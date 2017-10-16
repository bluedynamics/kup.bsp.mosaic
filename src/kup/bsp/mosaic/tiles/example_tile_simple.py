# -*- coding: utf-8 -*-
from plone.tiles import Tile

import random


class ExampleSimpleTile(Tile):

    @property
    def number(self):
        return random.randint(1000, 9999)
