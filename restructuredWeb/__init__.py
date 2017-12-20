#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from .adsense import setup as adsense_setup
from .configuration_block import setup as configuration_block_setup
from .codepen import setup as codepen_setup
from .gist import setup as gist_setup
from .layout import setup as layout_setup
from .jsfiddle import setup as jsfiddle_setup
from .javascript import setup as javascript_setup
from .css import setup as css_setup
from .ted import setup as ted_setup
from .twitter import setup as twitter_setup
from .youtube import setup as youtube_setup


def setup(app):
    adsense_setup(app)
    configuration_block_setup(app)
    codepen_setup(app)
    gist_setup(app)
    layout_setup(app)
    javascript_setup(app)
    jsfiddle_setup(app)
    css_setup(app)
    ted_setup(app)
    twitter_setup(app)
    youtube_setup(app)

    return {
        'version': '0.1',
        'parallel_read_safe': False,
        'parallel_write_safe': True
    }
