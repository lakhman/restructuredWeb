#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class javascript_node(nodes.Special, nodes.Inline, nodes.PreBibliographic,
                      nodes.FixedTextElement):
    pass


def visit_javascript_node(self, node):
    if 'inline' not in node:
        raise nodes.SkipNode

    self.body.append('\n<script type="text/javascript">\n')
    self.body.append(node.astext())

    raise nodes.SkipChildren


def depart_javascript_node(self, node):
    self.body.append('\n</script>\n')


class Javascript(Directive):
    """
    A js snippet for this specific document only
    Will be placed in the following block - within layout.html

    In layout.html, add/replace the following at the end of your </head>

    {%- if bootstrap_js_list %}
    <script type="text/javascript">
    {% for js in bootstrap_js_list -%}
    {{ js }}
    {% endfor -%}
    </script>
    {%- endif %}
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {'inline': directives.flag}

    def run(self):
        text = '\n'.join(self.content)
        node = javascript_node(text, text)

        if 'inline' in self.options:
            node['inline'] = self.options['inline']

        return [node]


def html_page_context(app, pagename, templatename, context, doctree):
    """
    Place JS into a bootstrap_js_list we can output in our template.
    """
    if 'bootstrap_js_list' not in context:
        context['bootstrap_js_list'] = []

    if doctree:
        js_nodes = doctree.traverse(javascript_node)
        for js in js_nodes:
            txt = js.astext()
            if 'inline' not in js:
                indent = '\n    '
                if len(context['bootstrap_js_list']) \
                        and txt[-5:-1] != indent:
                    context['bootstrap_js_list'][-1] += '\n'
                context['bootstrap_js_list'] += [txt.replace('\n', indent)]
                js.replace_self([])


def setup(app):
    app.connect('html-page-context', html_page_context)
    app.add_directive('javascript', Javascript)
    app.add_node(
        javascript_node, html=(visit_javascript_node, depart_javascript_node))
