#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from future.standard_library import install_aliases
install_aliases()

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from collections import OrderedDict
import re
from urllib.parse import urlencode

class youtube_video(nodes.General, nodes.Element):
    pass


def visit_youtube_video(self, node):
    classes = " ".join(node['classes'])
    node['classes'] = []

    self.body.append('<div class="{0}">'.format(classes))
    self.body.append(
        '<iframe allowfullscreen frameborder="0" src="%s">' % node['src'])
    self.body.append('</iframe>')
    self.body.append('</div>\n')

    raise nodes.SkipNode


def zero_one_choice(argument):
    return directives.choice(argument, ['0', '1'])


class Youtube(Directive):
    required_arguments = 0
    optional_arguments = 1
    has_content = False
    final_argument_whitespace = False

    # yapf: disable
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
        '4by3': directives.flag,

        # Youtube Options - https://developers.google.com/youtube/player_parameters
        # Choices instead of flags to keep things easy to remember
        'autoplay': zero_one_choice,  # 0 = no (default), 1 = yes
        'cc_load_policy': zero_one_choice,  # 0 = off, 1 = turn closed captions on
        'color': lambda x: directives.choice(x, ('red', 'white')),  # Progress bar color
        'controls': lambda x: directives.choice(x, ('0', '1', '2')),  # 0 = no controls, 1 = default (show)
        'disablekb': zero_one_choice,  # disable keyboard controls, 0 = false, 1 = true
        'enablejsapi': zero_one_choice,  # JS api control, 0 = false (default), 1 = true
        'end': directives.positive_int,  # duration to play and end video (in seconds)
        'fs': zero_one_choice,  # show full screen button, 0 = hide, 1 = display (default)
        'hl': directives.unchanged,  # interface language, an ISO 639-1 two-letter language code
        'iv_load_policy': lambda x: directives.choice(x, ('1', '3')),  # 1 = show (default), 3 = no show - Annotations
        'list': directives.unchanged_required,  # list for listType, search query, channel, playlist (with PL prefix)
        'listtype': lambda x: directives.choice(x, ('search', 'user_uploads', 'playlist')),  # view docs
        'loop': zero_one_choice,  # 0 = no (default), 1 = yes
        'modestbranding': zero_one_choice,  # show youtube video without logo (0 = no, 1 = yes)
        # 'origin': directives.unchanged_required,  # iframe security domain - fetched from configuration
        'playlist': directives.unchanged,  # list of video ids to embed, "id1,id2"
        'rel': zero_one_choice,  # show related videos at the end, 0 = no, 1 = yes
        'showinfo': zero_one_choice,  # 0 = hide, 1 = show (default)
        'start': directives.positive_int,  # duration to start playing video (in seconds)
        'theme': lambda x: directives.choice(x, ('light', 'dark')),  # dark,light - dark is default
        'autohide': zero_one_choice,  # 0 = visible, 1 = autohide - (Progress bar)
    }
    # yapf: enable

    def run(self):
        node = youtube_video('', **self.options)
        node['classes'] += self.options.get('class', [])
        youtube_id = None
        yt_base_embed = 'https://www.youtube.com/embed'
        is_list_type = 'list' in self.options and 'listtype' in self.options

        try:
            err = ValueError('Invalid Youtube ID')
            if self.arguments:
                youtube_id = directives.unchanged_required(self.arguments[0])
                regex = r"[a-zA-Z0-9_-]{11}"
                if not re.search(regex, youtube_id) and not is_list_type:
                    raise err
            elif not is_list_type:
                raise err
        except ValueError:
            err = 'Invalid Youtube ID attribute value for "%s" directive: "%s".'
            raise self.error(err % (self.name, self.arguments[0]
                                    if self.arguments else ''))

        if youtube_id and not is_list_type:
            node['src'] = yt_base_embed + "/{id}".format(id=youtube_id)
        else:
            node['src'] = yt_base_embed

        youtube_params = self.create_url_params(node)
        if len(youtube_params):
            node['src'] += '?%s' % youtube_params

        # ratio is done via Bootstrap class
        ratio = '16by9'
        if '4by3' in self.options:
            ratio = '4by3'

        node['classes'].insert(0, 'embed-responsive')
        node['classes'].insert(1, 'embed-responsive-%s' % ratio)

        self.add_name(node)
        return [node]

    def create_url_params(self, node):
        """
        Create and return a youtube url string to use to embed
        :param node: Our youtube_video node
        :return string: Youtube string
        """
        url_dict = OrderedDict()

        valid_option_list = [
            'autoplay', 'cc_load_policy', 'color', 'controls', 'disablekb',
            'enablejsapi', 'end', 'fs', 'hl', 'iv_load_policy', 'list',
            'listtype', 'loop', 'modestbranding', 'playlist', 'rel',
            'showinfo', 'start', 'theme', 'autohide'
        ]

        for option in valid_option_list:
            if option in self.options:
                if option == 'listtype':
                    url_dict['listType'] = self.options[option]
                else:
                    url_dict[option] = self.options[option]

        x = urlencode(url_dict)

        return x


def setup(app):
    app.add_config_value('youtube_origin_domain', None, True)  # rebuild
    app.add_node(youtube_video, html=(visit_youtube_video, None))
    app.add_directive('youtube', Youtube)
