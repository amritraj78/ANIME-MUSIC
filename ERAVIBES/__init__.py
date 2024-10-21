#
# Copyright (C) 2024 by amritraj78@Github, < https://github.com/amritraj78 >.
#
# This file is part of < https://github.com/amritraj78/ANIME-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/amritraj78/ANIME-MUSIC/blob/master/LICENSE >
#
# All rights reserved.

from ERAVIBES.core.bot import ERABot
from ERAVIBES.core.dir import dirr
from ERAVIBES.core.git import git
from ERAVIBES.core.userbot import Userbot
from ERAVIBES.misc import dbb, heroku, sudo

from .logging import LOGGER

# Bot Client

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

app = ERABot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
