import pychromecast
from .googletts import googleTTS_builder
import requests

name = "googlehomepush"
__all__ = (
    'GoogleHome',
)

class GoogleHome:
    """x
        Create a Google home (an host or a devicename is mandatory)
        :param devicename: string : the ip or device name of the Google Home
        :param host: the host of google home
        :param port: the port to contact google home by ip (default is 8009)
        :param ttsbuilder: function: the tts function. This is a function who have two parameter a text string and the lang. This function return an url to download mp3 file
    """
    def __init__(self, devicename = None, host = None, port = None, ttsbuilder = googleTTS_builder):
        if devicename != None:
            chromecasts = pychromecast.get_chromecasts()
            filteredChromeCast = filter(lambda c: c.host == devicename or c.device.friendly_name == devicename , chromecasts)
            
            try:
                self.cc = next(filteredChromeCast)
            except StopIteration:
                availbale_devices = list(map(lambda c: c.device.friendly_name, chromecasts))
                raise ValueError('Unable to found %s device. Available devices : %s'%(devicename, availbale_devices))
        elif host != None:
            self.cc = pychromecast.Chromecast(host, port)
        else:
            raise ValueError('host or devicename is mandatory to create a GoogleHome object.')

        self.ttsbuilder = ttsbuilder

    def say(self, text, lang = 'en-US'):
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=en-us&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        r = requests.get(url)
        self.play(url)

    def play(self, url, contenttype = 'audio/mp3'):
        self.cc.wait()
        mc = self.cc.media_controller
        mc.play_media(url, contenttype)
        mc.block_until_active()
        print("played url " + url)
