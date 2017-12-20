#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive


class layout_node(nodes.Special, nodes.Inline, nodes.PreBibliographic,
                  nodes.FixedTextElement):
    pass


def visit_layout_node(self, node):
    raise nodes.SkipNode


class Layout(Directive):
    """
    Switch and render this document in another layout
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}

    def run(self):
        text = '\n'.join(self.content)
        node = layout_node(text, text)
        node['layout'] = self.arguments[0]

        return [node]


def html_page_context(app, pagename, templatename, context, doctree):
    if doctree:
        layout_nodes = doctree.traverse(layout_node)

        if len(layout_nodes) > 1:
            app.builder.warn('Multiple .. layout:: nodes detected in %s:%s',
                             (app.builder.current_docname,
                              layout_nodes[0].line))

        if len(layout_nodes) > 0:
            for layout in layout_nodes:
                layout.replace_self([])
            return layout_nodes[0]['layout']


def setup(app):
    app.connect('html-page-context', html_page_context)
    app.add_directive('layout', Layout)
    app.add_node(layout_node, html=(visit_layout_node, None))
