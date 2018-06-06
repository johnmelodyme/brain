# SoundDevicePlayer

SoundDevicePlayer is based on the [SoundDevice and SoundFile engines](https://pypi.python.org/pypi/sounddevice).

## Options

| Parameters | Required | Default | Choices    | Comment |
|------------|----------|---------|------------|---------|
| convert_to_wav | no        | TRUE      | True, False | Convert the generated file from the TTS into wav before reading |

## Example Settings

``` yaml
default_player: "sounddeviceplayer"

players:  
  - sounddeviceplayer:
     convert_to_wav: True
```

## Notes

SoundDevicePlayer does not handle mp3 format, converting mp3 to wav might be required.
