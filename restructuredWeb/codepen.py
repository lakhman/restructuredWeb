#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
import re

DEFAULT_CODEPEN_THEME = 'light'


class Codepen(Directive):
    """
    Codepen Directive
    """
    required_arguments, optional_arguments = 1, 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {
        'height': directives.length_or_percentage_or_unitless,
        'preview': directives.flag,
        'theme': directives.unchanged,
        'tabs': directives.unchanged,
    }

    theme = None

    def run(self):
        if hasattr(self.state.document.settings, 'env'):
            env = self.state.document.settings.env
            codepen_theme = env.app.config.codepen_theme
        else:
            codepen_theme = DEFAULT_CODEPEN_THEME

        node = codepen()
        node['theme'] = codepen_theme

        # Overrides the app config
        if 'theme' in self.options:
            node['theme'] = self.options.get('theme')

        if 'preview' in self.options:
            node['preview'] = self.options.get('preview')

        if 'height' in self.options:
            node['height'] = self.options.get('height')

        if 'tabs' in self.options:
            node['tabs'] = self.options.get('tabs')

        try:
            if self.arguments:
                url_match = re.match(
                    r"^https://codepen\.io/(.+[^/])/pen/(.+[^/])/?$",
                    self.arguments[0])
                if url_match and len(url_match.groups()):
                    node['url'] = self.arguments[0]
                    node['author'] = url_match.group(1)
                    node['slug'] = url_match.group(2)
                else:
                    raise ValueError('Invalid Codepen URL.')
        except ValueError as err:
            e = '%s for "%s" directive: "%s".'
            raise self.error(e % (err, self.name,
                                  self.arguments[0]))

        return [node] + []


class codepen(nodes.Element):
    pass


def visit_codepen(self, node):
    atts = ['data-embed-version="2"']

    if 'height' in node:
        px = directives.length_or_percentage_or_unitless(node['height'], 'px')
        atts.append(
            'data-height="{}" style="height: {};"'.format(node['height'], px))
    else:
        atts.append(
            'data-height="{}" style="height: {};"'.format('265', '265px'))

    if 'author' in node and 'slug' in node:
        atts.append('data-slug-hash="{}"'.format(node['slug']))
        atts.append('data-user="{}"'.format(node['author']))

    if 'theme' in node:
        atts.append('data-theme-id="{}"'.format(node['theme']))

    if 'preview' in node:
        atts.append('data-preview="true"')

    if 'tabs' in node:
        atts.append('data-default-tab="{}"'.format(node['tabs']))

    props = " ".join(atts)

    node = '<div class="rst-codepen"><p class="codepen" {}>{}</p></div>'.format(
        props, node['url'])
    self.body.append(node + '\n')

    raise nodes.SkipNode


def setup(app):
    app.add_config_value('codepen_theme', DEFAULT_CODEPEN_THEME, 'env')
    app.add_directive('codepen', Codepen)
    app.add_node(codepen, html=(visit_codepen, None))
