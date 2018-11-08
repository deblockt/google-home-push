# Google home push

Library for Python 3.4+ to push text message or audio file with the Google Home.

## Installation

    pip install googlehomepush

version: 0.0.3

## Dependencies

PyChromecast depends on the Python packages gTTS, pychromecast. Make sure you have these dependencies installed using `pip install -r requirements.txt`

## How to use

``` python
from googlehomepush import GoogleHome

GoogleHome("LivingRoom").say("test")
GoogleHome("LivingRoom").play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3")
```

## API

### GoogleHome(deviceIdentifier, tts_builder = googleTTS_Builder)

Create a new Google Home `instance`. 
- `deviceIdentifier` can be the google home name, or its IP.
- `tts_builder` the tss engine to use. Available tts are:
    - `googleTTS_Builder` import with `from googlehomepush.googletts import googleTTS_builder`. Free TTS used by google translate. It's the default engine
    - `googlecloudTTS_builder` import with `from googlehomepush.googlecloudTTS import googlecloudTTS_builder`. Google cloud TTS engine. See https://cloud.google.com/text-to-speech/docs/reference/libraries to create an account.

### .say(text, lang = 'en-US')

Push a message on Google home

- `text` is the test message to say
- `lang` the text language, default value is 'en'

### .play(url, contentType = 'audio/mp3'):

Push a sond to Google home
- `url` an audio file URL
- `contentType` the audi file content type

You can play a local file using `http_server` 

``` python
from googlehomepush.http_server import serve_file

file_url = serve_file("/path/to/file", "audio/mp3")
GoogleHome("LivingRoom").play(file_url, "audio/mp3")
```

## Maintainers

- Thomas Deblock (@tdeblock)
