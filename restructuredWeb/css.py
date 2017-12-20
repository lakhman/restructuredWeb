#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive


class css_node(nodes.Special, nodes.Inline, nodes.PreBibliographic,
               nodes.FixedTextElement):
    pass


def visit_css_node(self, node):
    raise nodes.SkipNode


class Css(Directive):
    """
    A css snippet for this specific document only
    Will be placed in the following block - within layout.html

    In layout.html, add/replace the following at the end of your </head>

    {% block extrahead -%}
    {%- if bootstrap_css_list %}
    <style type="text/css">
    {% for css in bootstrap_css_list -%}
    {{ css }}
    {% endfor -%}
    </style>
    {%- endif %}
    {%- endblock %}
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {}

    def run(self):
        text = '\n'.join(self.content)
        node = css_node(text, text)

        return [node]


def html_page_context(app, pagename, templatename, context, doctree):
    """
    Place CSS into a bootstrap_css_list we can output in our template.
    """

    if 'bootstrap_css_list' not in context:
        context['bootstrap_css_list'] = []

    if doctree:
        css_nodes = doctree.traverse(css_node)
        for css in css_nodes:
            txt = css.astext()
            indent = '\n    '
            if len(context['bootstrap_css_list'])\
                    and txt[-5:-1] != indent:
                context['bootstrap_css_list'][-1] += '\n'
            context['bootstrap_css_list'] += [txt.replace('\n', indent)]
            css.replace_self([])


def setup(app):
    app.connect('html-page-context', html_page_context)
    app.add_directive('css', Css)
    app.add_node(css_node, html=(visit_css_node, None))
