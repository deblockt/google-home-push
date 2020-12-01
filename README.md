[![PyPI version](https://badge.fury.io/py/googlehomepush.svg)](https://badge.fury.io/py/googlehomepush)

# Google home push

Library for Python 3.8+ to push text message or audio file with the Google Home.

## Installation

    pip install (not done yet making a pypi v2 of googlehomepush)

## Dependencies

None for now

## How to use

``` python
from googlehomepush import GoogleAssistant
from googlehomepush.http_server import serve_file # for local files
host = "ip"
home = GoogleAssistant(host=host)
home.say("test")
home.play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3")

file_url = serve_file("/path/to/file", "audio/mp3") # local
home.play(file_url, "audio/mp3")
home.volume(100)
home.volume(0)

```
### .say(text, speed, lang)

Push a message on Google home

- `text` is the test message to say
- `speed` is the rate of speed of the message ranges from 0.000+ as slowest to 1 as normal speed.
- `lang` the text language, default value is 'en' to change it have lang = 'language' as described in google translate en-Us, es (spanish), ect

### .play(url, contentType = 'audio/mp3'):

Push a sound to Google home
- `url` an audio file URL
- `contentType` the audio file content type

### .volume(volumelevel):
- `volumelevel` the volume level from 0-100 by 0.01 to 1 Example: home.volume(volumelevel=0.05 or 5 percent volume. If you want to take it as user input you can do volumelevel=float(input()) the float is required to convert it as it is a decimal.



## Maintainers

- Thomas Deblock (@tdeblock)
- Dray-Cyber aswell!
