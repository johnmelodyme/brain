# PyAudioPlayer

PyAudioPlayer is based on the [PyAudio engine](https://people.csail.mit.edu/hubert/pyaudio/).

## Options

| Parameters | Required | Default | Choices    | Comment |
|------------|----------|---------|------------|---------|
| convert_to_wav | no        | TRUE      | True, False | Convert the generated file from the TTS into wav before reading |

## Example Settings

``` yaml
default_player: "pyaudioplayer"

players:  
  - pyaudioplayer:
     convert_to_wav: True
```

## Notes

PyAudioPlayer does not handle mp3 format, converting mp3 to wav might be required.
