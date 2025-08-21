# All rights reserved.
#

from .Apple import Apple as apple
from .Carbon import Carbon as carbon
from .JioSavan import Saavn as saavn
from .Resso import Resso as resso
from .Soundcloud import SoundCloud as soundcloud
from .Spotify import Spotify as spotify
from .Telegram import Telegram as telegram
from .Youtube import YouTube as youtube


class PlaTForms:
    def __init__(self):
        self.apple = apple()
        self.carbon = carbon()
        self.saavn = saavn()
        self.resso = resso()
        self.soundcloud = soundcloud()
        self.spotify = spotify()
        self.telegram = telegram()
        self.youtube = youtube()
