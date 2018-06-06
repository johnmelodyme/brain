# PyAlsaAudio

PyAlsaAudio is based on the [Alsa engine](https://larsimmisch.github.io/pyalsaaudio/libalsaaudio.html).

## Options

| Parameters | Required | Default | Choices    | Comment |
|------------|----------|---------|------------|---------|
| device         | no        | "default" |             | Select the device to use for alsa                               |
| convert_to_wav | no        | TRUE      | True, False | Convert the generated file from the TTS into wav before reading |

## Example Settings

``` yaml
default_player: "pyalsaaudio"

players:
  - pyalsaaudio:
     device: "default"
     convert_to_wav: True
```

## Notes

Define the default card to use in the `device` parameter.
For example, on a Raspberry Pi, the default card can be `sysdefault:CARD=ALSA`.

PyAlsaAudio does not handle mp3 format, converting mp3 to wav might be required if the selected TTS engine generates a mp3 file.
