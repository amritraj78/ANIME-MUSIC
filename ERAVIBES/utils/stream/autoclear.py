#
# Copyright (C) 2024 by amritraj78@Github, < https://github.com/amritraj78 >.
#
# This file is part of < https://github.com/amritraj78/ANIME-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/amritraj78/ANIME-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
