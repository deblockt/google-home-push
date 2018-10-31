# Google home push

Library for Python 3.4+ to push text message or audio file with the Google Home.

## Installation

    pip install googlehomepush

## Dependencies

PyChromecast depends on the Python packages gTTS, pychromecast. Make sure you have these dependencies installed using `pip install -r requirements.txt`

## How to use

``` python
from googlehomepush import GoogleHome

GoogleHome("LivingRoom").say("test")
GoogleHome("LivingRoom").play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3")
```

## API

### GoogleHome(deviceIdentifier)

Create a new Google Home `instance`. 
- `deviceIdentifier` can be the google home name, or its IP.

### .say(text, lang = 'en', slow = False)

Push a message on Google home

- `text` is the test message to say
- `lang` the text language, default value is 'en'
- `slow` true if you want the message to be delivered slowly

### .play(url, contentType = 'audio/mp3'):

Push a sond to Google home
- `url` an audio file URL
- `contentType` the audi file content type

## Maintainers

- Thomas Deblock (@tdeblock)
