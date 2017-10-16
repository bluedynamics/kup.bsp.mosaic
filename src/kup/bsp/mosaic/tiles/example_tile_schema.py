# -*- coding: utf-8 -*-
from plone.supermodel.model import Schema
from plone.tiles import Tile
from zope import schema


class IExampleTile(Schema):

    tickerline = schema.TextLine(
        title=u'Ticker Line',
        description=u'A ticker line',
        required=True,
    )
    red = schema.Bool(
        title=u'Red Color?',
        default=False,
        required=False,
    )


class ExampleSchemaTile(Tile):

    @property
    def show_red(self):
        return self.data['red']

    @property
    def tickerline(self):
        return self.data['tickerline']
