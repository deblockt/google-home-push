import pychromecast
from .googletts import GoogleTTS

name = "googlehomepush"
__all__ = (
    'GoogleHome',
)

class GoogleHome:

    def __init__(self, devicename):
        chromecasts = pychromecast.get_chromecasts()
        filteredChromeCast = filter(lambda c: c.host == devicename or c.device.friendly_name == devicename , chromecasts)
        
        try:
            self.cc = next(filteredChromeCast)
        except StopIteration:
            availbaleDevices = list(map(lambda c: c.device.friendly_name, chromecasts))
            raise ValueError('Unable to found %s device. Available devices : %s'%(devicename, availbaleDevices))

    def say(self, text, lang = 'en', slow = False):
        tts = GoogleTTS(text=text, lang=lang, slow=slow)
        self.play(tts.url())

    def play(self, url, contentType = 'audio/mp3'):
        self.cc.wait()
        mc = self.cc.media_controller
        mc.play_media(url, contentType)
        mc.block_until_active()
        print("played url " + url)