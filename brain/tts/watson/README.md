# Watson

Watson TTS is based on the [Watson API](https://www.ibm.com/watson/services/text-to-speech/).

## Options

| Parameters | Required | Default | Choices    | Comment |
|------------|----------|---------|------------|---------|
| username   | yes      |         |                       | Username of the created service in IBM cloud      |
| password   | yes      |         |                       | Password related to the username                  |
| voice      | yes      |         | See voice table below | Code that define the voice used for the synthesis |

## Voice Codes

| Languages              | Code                             | Gender |
|------------------------|----------------------------------|--------|
| German                 | de-DE_BirgitVoice                | Female |
| German                 | de-DE_DieterVoice                | Male   |
| UK English             | en-GB_KateVoice                  | Female |
| US English             | en-US_AllisonVoice               | Female |
| US English             | en-US_LisaVoice                  | Female |
| US English             | en-US_MichaelVoice (the default) | Male   |
| Castilian Spanish      | es-ES_EnriqueVoice               | Male   |
| Castilian Spanish      | es-ES_LauraVoice                 | Female |
| Latin American Spanish | es-LA_SofiaVoice                 | Female |
| North American Spanish | es-US_SofiaVoice                 | Female |
| French                 | fr-FR_ReneeVoice                 | Female |
| Italian                | it-IT_FrancescaVoice             | Female |
| Japanese               | ja-JP_EmiVoice                   | Female |
| Brazilian Portuguese   | pt-BR_IsabelaVoice               | Female |

## Example Settings

``` yaml
default_text_to_speech: "watson"
cache_path: "/tmp/assistant_tts_cache"
text_to_speech:
  - watson:
      username: "username_code"
      password: "generated_password"
      voice: "fr-FR_ReneeVoice"
```
