#
# Copyright (C) 2024 by amritraj78@Github, < https://github.com/amritraj78 >.
#
# This file is part of < https://github.com/amritraj78/ANIME-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/amritraj78/ANIME-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
