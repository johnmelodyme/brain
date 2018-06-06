# Brain

Update your brain from a neuron

Current actions available:
- enable / disable a synapse from the brain

## Options

| Parameter    | Required | Type    | Default | Choices     | Comment                           |
|--------------|----------|---------|---------|-------------|-----------------------------------|
| synapse_name | YES      | string  |         |             | The name of the synapse to update |
| enabled      | YES      | boolean |         | True, False | if True, the synapse is enabled.  |

## Return Values

| Name         | Description                | Type    | Sample                      |
|--------------|----------------------------|---------|-----------------------------|
| synapse_name | The updated synapse name   | string  | to-deactivate               |
| status       | New status of the synapse  | boolean | enabled, disabled, unknown  |

## Synapses Example

```yml
- name: "to-deactivate"
  signals:
    - order: "who am I"
  neurons:
    - say:
        message: "you are Batman"

- name: "deactivate"
  signals:
    - order: "deactivate a synapse"
  neurons:
    - brain:
        synapse_name: "to-deactivate"
        enabled: False

- name: "activate"
  signals:
    - order: "active back the synapse"
  neurons:
    - brain:
        synapse_name: "to-deactivate"
        enabled: True
```

## Notes

> Changes made to the brain from this neuron are not persistent. The brain will be loaded again following the yaml file at the next start of Brain.ai.
