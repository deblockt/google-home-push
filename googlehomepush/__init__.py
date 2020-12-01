import pychromecast
import requests as req
name = "googlehomepush"
__all__ = 'GoogleHome'
class GoogleHome:
    def __init__(self, host = None):
        try:
            if host != None:
                self.cc = pychromecast.Chromecast(host)
            else:
                print('For a host input the ip and have the option like: host = "192.168.0.whatever" home = GoogleHome(host=host) ')
        except:
            print("Some sort of error occured")
    def play(self, url, contenttype = 'audio/mp3'):
        self.cc.wait()
        mc = self.cc.media_controller
        mc.play_media(url, contenttype)
        mc.block_until_active()
    def say(self, text, lang = 'en-US'):
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=" + lang + "&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        r = req.get(url)
        self.play(url)
    def volume(self, volume):
        self.cc.set_volume(volume)
