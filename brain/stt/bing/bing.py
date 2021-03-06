import speech_recognition as sr

from brain.core import Utils
from brain.stt.Utils import SpeechRecognition


class Bing(SpeechRecognition):

    def __init__(self, callback=None, **kwargs):
        """
        Start recording the microphone and analyse audio with Bing api
        :param callback: The callback function to call to send the text
        :param kwargs:
        """
        # give the audio file path to process directly to the mother class if exist
        SpeechRecognition.__init__(self, kwargs.get('audio_file_path', None))

        # callback function to call after the translation speech/tex
        self.main_controller_callback = callback
        self.key = kwargs.get('key', None)
        self.language = kwargs.get('language', "en-US")
        self.show_all = kwargs.get('show_all', False)

        # start listening in the background
        self.set_callback(self.bing_callback)
        # start processing, record a sample from the microphone if no audio file path provided, else read the file
        self.start_processing()

    def bing_callback(self, recognizer, audio):
        """
        called from the background thread
        """
        try:
            captured_audio = recognizer.recognize_bing(audio,
                                                       key=self.key,
                                                       language=self.language,
                                                       show_all=self.show_all)
            Utils.print_info("Speech to Text Engine: Bing thinks you said %s" % captured_audio)
            self._analyse_audio(captured_audio)

        except sr.UnknownValueError:
            Utils.print_warning("Speech to Text Engine: Bing could not understand audio")
            # callback anyway, we need to listen again for a new order
            self._analyse_audio(audio_to_text=None)
        except sr.RequestError as e:
            Utils.print_danger("Speech to Text Engine: could not request results from Bing; {0}".format(e))
            # callback anyway, we need to listen again for a new order
            self._analyse_audio(audio_to_text=None)
        except AssertionError:
            Utils.print_warning("Speech to Text Engine: no audio caught from microphone")
            self._analyse_audio(audio_to_text=None)

    def _analyse_audio(self, audio_to_text):
        """
        Confirm the audio exists and run it in a Callback
        :param audio_to_text: the captured audio
        """
        if self.main_controller_callback is not None:
            self.main_controller_callback(audio_to_text)
