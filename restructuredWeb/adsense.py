#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


class Adsense(Directive):
    """
    Adsense Directive
    """

    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = False
    has_content = False
    option_spec = {
        'format': directives.class_option,
        'class': directives.class_option
    }

    def run(self):
        node = adsense()

        if self.arguments:
            node.attributes['data-ad-slot'] = self.arguments[0]
        else:
            node.attributes['data-ad-slot'] = False

        # Default to auto if nothing passed by user
        node['data-ad-format'] = self.options.get('format', 'auto')
        node['classes'] += self.options.get('class', [])

        return [node] + []


class adsense(nodes.Element):
    pass


def visit_adsense(self, node):
    client_id = self.builder.config['adsense_client_id']
    if not client_id:
        self.builder.app.warn(
            'adsense_client_id was False, check your conf.py. ["%s"]' %
            self.builder.current_docname)
        raise nodes.SkipNode

    user_slots = self.builder.config['adsense_slots']
    ad_slot = node.attributes['data-ad-slot']

    # Use default slot if nothing was passed
    if not node.attributes['data-ad-slot']:
        ad_slot = self.builder.config['adsense_default_slot']

    # Load from our user slot list if we have one
    if user_slots:
        for slot in user_slots:
            if slot == ad_slot:
                ad_slot = user_slots[slot]

    if not ad_slot or not ad_slot.isdigit():
        self.builder.app.warn('Skipping adsense slot as it\'s invalid in "%s"'
                              % self.builder.current_docname)
        raise nodes.SkipNode

    raw_tpl = '<ins class="adsbygoogle" style="display:block" ' \
              'data-ad-client="%s" data-ad-slot="%s" data-ad-format="%s"></ins>'
    tpl = raw_tpl % (client_id, ad_slot, node.attributes['data-ad-format'])

    if node['classes']:  # Add a wrapping div
        self.body.append('<div class="%s">\n%s\n</div>\n' %
                         (' '.join(node['classes']), tpl))
    else:  # Regular Adsense snippet (no wrapping)
        self.body.append(tpl + '\n')

    raise nodes.SkipNode


def setup(app):
    app.add_directive('adsense', Adsense)
    app.add_config_value('adsense_client_id', '', 'html')
    app.add_config_value('adsense_slots', {}, 'html')
    app.add_config_value('adsense_default_slot', '', 'html')
    app.add_node(adsense, html=(visit_adsense, None))
