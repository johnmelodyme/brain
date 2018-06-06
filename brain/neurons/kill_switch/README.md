# Kill Switch

This neuron exits the Brain.ai process.

## Synapses Example

Simple example :

```yml
  - name: "stop-brain"
    signals:
      - order: "goodbye"
    neurons:
      - kill_switch    
```
