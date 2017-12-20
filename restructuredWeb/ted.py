#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
import re


class ted_video(nodes.General, nodes.Element):
    pass


def visit_ted_video(self, node):
    classes = " ".join(node['classes'])
    node['classes'] = []

    self.body.append('<div class="{0}">\n'.format(classes))
    self.body.append(
        '<iframe frameborder="0" scrolling="no" allowfullscreen src="%s">' %
        node['src'])
    self.body.append('</iframe>\n')
    self.body.append('</div>\n')

    raise nodes.SkipNode


class Ted(Directive):
    required_arguments, optional_arguments = 0, 1
    has_content = False
    final_argument_whitespace = False

    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
        '4by3': directives.flag,
    }

    def run(self):
        if not len(self.arguments):
            raise self.error(
                "No argument provided for %s directive." % self.name)

        node = ted_video('', **self.options)
        node['classes'] += self.options.get('class', [])
        embed_arg = self.arguments[0]
        replaced = re.sub('https://www.ted', 'https://embed.ted', embed_arg)
        node['src'] = replaced

        ratio = '16by9'
        if '4by3' in self.options:
            ratio = '4by3'

        node['classes'].insert(0, 'embed-responsive')
        node['classes'].insert(1, 'embed-responsive-%s' % ratio)

        self.add_name(node)
        return [node]


def setup(app):
    app.add_node(ted_video, html=(visit_ted_video, None))
    app.add_directive('ted', Ted)
