# Event

An **event** is a way to schedule the launching of a synapse periodically at fixed times, dates, or intervals.

The event system is based on [APScheduler](http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html) which is itself based on [Linux crontab](https://en.wikipedia.org/wiki/Cron). 
When you declare an event in the signal, Brain.ai will schedule the launching of the target synapse.

The syntax of an event declaration in a synapse is:

``` yaml
signals:
  - event:
      parameter1: "value1"
      parameter2: "value2"
```

For example, if we want Brain.ai to run the synapse every day a 8:30, the event will be declared like:

``` yaml
- event:
    hour: "8"
    minute: "30"
```

## Options

Parameters are keywords you can use to build your event.

List of available parameter:

| parameter   | required | default | choices                                                         | comment   |
|-------------|----------|---------|-----------------------------------------------------------------|-----------|
| year        | no       | *       | 4 digit                                                         | E.g: 2016 |
| month       | no       | *       | month (1-12)                                                    |           |
| day         | no       | *       | day of the (1-31)                                               |           |
| week        | no       | *       | ISO week (1-53)                                                 |           |
| day_of_week | no       | *       | number or name of weekday  (0-6 or mon,tue,wed,thu,fri,sat,sun) | 6=Sunday  |
| hour        | no       | *       | hour (0-23)                                                     |           |
| minute      | no       | *       | minute (0-59)                                                   |           |
| second      | no       | *       | second (0-59)                                                   |           |

> You must set at least one parameter from the list of parameter

Expressions can be used in value of each parameter. Multiple expression can be given in a single field, separated by commas.

| Expression | Field | Description                                                                             |
|------------|-------|-----------------------------------------------------------------------------------------|
| *          | any   | Fire on every value                                                                     |
| */a        | any   | Fire every `a` values, starting from the minimum                                        |
| a-b        | any   | Fire on any value within the `a-b` range (a must be smaller than b)                     |
| a-b/c      | any   | Fire every c values within the `a-b` range                                              |
| xrd y      | day   | Fire on the `x` -rd occurrence of weekday `y` within the month                          |
| last x     | day   | Fire on the last occurrence of weekday `x` within the month                             |
| last x     | day   | Fire on the last day within the month                                                   |
| x,y,z      | day   | Fire on any matching expression; can combine any number of any of the above expressions |


## Synapses Example

### Web clock radio

Let's make a complete example. We want Brain.ai to wake us up each morning of working day (Monday to friday) at 7:30 AM and:
- Wish us good morning
- Give us the time
- Play our favourite web radio

The synapse in the brain would be:

``` yaml
  - name: "wake-up"
    signals:
      - event:
          hour: "7"
          minute: "30"
          day_of_week: "1,2,3,4,5"
    neurons:
      - say:
          message:
            - "Good morning"
      - system_time_date:
          say_template:
            - "It is {{ hours }} hours and {{ minutes }} minutes."
      - shell: 
          cmd: "mplayer http://192.99.17.12:6410/"
          async: True
```

After setting up an event, you must restart Brain.ai.

```bash
brain start
```

If the syntax is good, Brain.ai will show you each synapse that it has loaded in the crontab.
```
Add synapse name "wake-up" to the scheduler: cron[day_of_week='1,2,3,4,5', hour='7', minute='30']
Event loaded
```
That's it, the synapse is now scheduled and will be started automatically.
