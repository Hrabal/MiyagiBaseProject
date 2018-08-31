# -*- coding: utf-8 -*-
from Miyagi import App

from public import frontend

app = App(config='config.yml', custom_pages=[frontend, ])
