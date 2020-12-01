[![PyPI version](https://badge.fury.io/py/googlehomepush.svg)](https://badge.fury.io/py/googlehomepush)

# Google home push

Library for Python 3.8+ to push text message or audio file with the Google Home.

## Installation

    pip install googlehomepush

## Dependencies

None for now

## How to use

``` python
from googlehomepush import GoogleHome
from googlehomepush.http_server import serve_file # for local files
host = "ip"
home = GoogleHome(host=host)
home.say("test")
home.play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3")

file_url = serve_file("/path/to/file", "audio/mp3") # local
home.play(file_url, "audio/mp3")
home.volume(100)
home.volume(0)

```
### .say(text, lang = 'en-US')

Push a message on Google home

- `text` is the test message to say
- `lang` the text language, default value is 'en'

### .play(url, contentType = 'audio/mp3'):

Push a sound to Google home
- `url` an audio file URL
- `contentType` the audi file content type

### .volume(volumelevel):
- `volumelevel` the volume level from 0-100 by 0.01 to 1




## Maintainers

- Thomas Deblock (@tdeblock)
- Dray-Cyber aswell!
