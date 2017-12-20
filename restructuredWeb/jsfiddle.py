#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import re


class JSFiddle(Directive):
    """
    JSFiddle Directive
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = False
    has_content = False
    option_spec = {'height': directives.length_or_percentage_or_unitless}

    def run(self):
        node = jsfiddle()

        if self.arguments:
            url = re.sub('^(http)?s?:?//', '', self.arguments[0])
            node['src'] = url

        if 'height' in self.options:
            node['height'] = self.options['height']

        return [node] + []


class jsfiddle(nodes.Element):
    pass


def visit_jsfiddle(self, node):
    height = node['height'] if 'height' in node else '300'
    tpl = '<div class="rst-jsfiddle">\n' \
          '<iframe src="//{}" width="99.9%" height="{}" ' \
          'allowfullscreen="allowfullscreen" frameborder="0"></iframe>\n' \
          '</div>\n'
    self.body.append(tpl.format(node['src'], height))

    raise nodes.SkipNode


def setup(app):
    app.add_directive('jsfiddle', JSFiddle)
    app.add_node(jsfiddle, html=(visit_jsfiddle, None))
