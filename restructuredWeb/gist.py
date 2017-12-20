#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive
import re


class Gist(Directive):
    """
    Gist Directive
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = False

    def run(self):
        node = gist()

        try:
            if self.arguments:
                url_match = re.match(
                    r"(<script src=\")?"
                    r"(https://gist\.github\.com/[^\">]+)"
                    r"(\"></script>)?",
                    self.arguments[0])
                if url_match and len(url_match.groups()):
                    script_tag = url_match.group(1)
                    base_gist_url = url_match.group(2)
                    if script_tag:
                        err = 'Remove the script tag from gist url.'
                        raise ValueError(err)

                    if not base_gist_url.endswith('.js'):
                        base_gist_url += '.js'

                    node['src'] = base_gist_url
                else:
                    raise ValueError('Invalid Github gist URL.')
        except ValueError as err:
            e = '%s for "%s" directive: "%s".'
            raise self.error(e % (err, self.name,
                                  self.arguments[0]))

        return [node] + []


class gist(nodes.Element):
    pass


def visit_gist(self, node):
    tpl = '<div class="rst-gist"><script src="%s"></script></div>' % node[
        'src']
    self.body.append(tpl + '\n')

    raise nodes.SkipNode


def setup(app):
    app.add_directive('gist', Gist)
    app.add_node(gist, html=(visit_gist, None))
