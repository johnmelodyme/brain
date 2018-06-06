# Say

This neuron is the mouth of Brain.ai and uses the [TTS](../../Docs/tts.md) to say the given message.

## Options

| Parameter | Required | Default | Choices | Comment                                                    |
|-----------|----------|---------|---------|------------------------------------------------------------|
| message   | YES      |         |         | A single message or a list of messages Brain.ai could say  |

## Synapses Example

Simple example :

```yml
- name: "Say-hello"
  signals:
    - order: "hello"
  neurons:
    - say:
        message: "Hello Sir"     
```

With a multiple choice list, Brain.ai will pick one randomly:

```yml
- name: "Say-hello"
  signals:
    - order: "hello"
  neurons:
    - say:
        message:
          - "Hello Sir"
          - "Welcome Sir"
          - "Good morning Sir"
```

With an input value
```yml
- name: "Say-hello-to-friend"
  signals:
    - order: "say hello to {{ friend_name }}"
  neurons:
    - say:
        message: "Hello {{ friend_name }}"
```

## Notes

> The neuron does not return any values.
> Brain.ai randomly takes a message from the list
