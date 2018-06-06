# Sleep

This neuron sleeps the system for a given time in seconds.

## Options

| Parameter | Required | Default | Choices | Comment                         |
|-----------|----------|---------|---------|---------------------------------|
| seconds   | YES      |         |         | The number of seconds to sleep. |

## Synapses Example

Simple example :

```yml
  - name: "run-simple-sleep"
    signals:
      - order: "Wait for me "
    neurons:
      - sleep:
          seconds: 60
```
