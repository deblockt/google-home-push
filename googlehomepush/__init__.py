import pychromecast
from .googletts import googleTTS_builder

name = "googlehomepush"
__all__ = (
    'GoogleHome',
)

class GoogleHome:

    def __init__(self, devicename, ttsbuilder = googleTTS_builder):
        """
        Create a Google home
        devicename: string : the ip or device name of the Google Home
        ttsbuilder: function: the tts function. This is a function who have two parameter a text string and the lang. This function return an url to download mp3 file
        """
        chromecasts = pychromecast.get_chromecasts()
        filteredChromeCast = filter(lambda c: c.host == devicename or c.device.friendly_name == devicename , chromecasts)
        
        try:
            self.cc = next(filteredChromeCast)
        except StopIteration:
            availbale_devices = list(map(lambda c: c.device.friendly_name, chromecasts))
            raise ValueError('Unable to found %s device. Available devices : %s'%(devicename, availbale_devices))

        self.ttsbuilder = ttsbuilder

    def say(self, text, lang = 'en-US'):
        ttsurl = self.ttsbuilder(text, lang)
        self.play(ttsurl)

    def play(self, url, contenttype = 'audio/mp3'):
        self.cc.wait()
        mc = self.cc.media_controller
        mc.play_media(url, contenttype)
        mc.block_until_active()
        print("played url " + url)