# Deaf

Deaf control of brain. If set to True the trigger process will be stopped.

Once this neuron is used, and Brain.ai deaf, the hotword is deactivated. Only ways to undeaf are:
- by calling the API (see [deaf section](../../../Docs/rest_api.md#switch-deaf-status))
- If running on Raspberry, by using the undeaf button. (See the section [Raspberry LED and deaf button](../../../Docs/settings.md#raspberry-led-and-deaf-button))
- by using another signals than a "vocal order" that call back this neuron with a status set to "False"
- Restarting Brain.ai

## Options

| Parameter | Required | Type    | Default | Choices     | Comment                                           |
|-----------|----------|---------|---------|-------------|---------------------------------------------------|
| status    | YES      | Boolean |         | True, False | If "True" Brain.ai will stop the hotword process  |


## Synapses Example

Deaf Brain.ai from a vocal order
```yml
- name: "deaf-synapse"
  signals:
    - order: "stop listening"
  neurons:
    - say:
        message:
          - "I stop hearing you, sir"
    - deaf:
        status: True
```

Undeaf Brain.ai from another signals. In the following example, a MQTT message is received
```yml
- name: "undeaf-synapse"
  signals:
    - mqtt_subscriber:
        broker_ip: "127.0.0.1"
        topic: "/my/sensor"
  neurons:
    - deaf:
        status: False
    - say:
        message:
          - "Waiting for orders, sir"
```
