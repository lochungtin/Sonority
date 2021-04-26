<img src="./img/SonorityLogo.png" style="height: 150px">

## Sonority
Multi-Channel Ping Alarm Scheduler for Discord Servers

Sonority is a discord alarm bot coded in discord.py with virtually infinite alarm channels.

### Alarm Types
- Timer - Expires after duration
- Alarm - Expires when date/time is reached

### Usage
#### Setting a timer
```
s.timer duration [-option] [*description]
```
```
Example 1: s.timer 1:30:00 -D this sets a timer for 1hr and 30 mins
Example 2: s.timer 5:00 -M this set a timer for 5 mins

duration:
    *d?:*h?:*m?:s
    * 0 or more characters

option: (optional)
    -D / -d - Ping in desktop only channel
    -M / -m - Ping in mobile only channel
    
description: (optional)
    string of words describing the event for the timer
```

#### Setting an alarm
```
s.alarm time [date] [-option] [*description]
```
```
Example 1: s.alarm 1:30:00 -D this sets a timer for 1hr and 30 mins
Example 2: s.timer 5:00 -M this set a timer for 5 mins

time: hh:mm:ss (24 hour military time)

date: YYYY:MM:DD

option: (optional) same as timer
    
description: (optional) same as timer
```