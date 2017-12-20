# -*- coding: utf-8 -*-
"""
Copyright (c) 2010-2017 Fabien Potencier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

:copyright: (c) 2010-2017 Fabien Potencier
:license: MIT, see LICENSE for more details.
:url: https://github.com/fabpot/sphinx-php/blob/master/LICENSE
"""
from docutils.parsers.rst import Directive
from docutils import nodes


class configurationblock(nodes.General, nodes.Element):
    pass


class ConfigurationBlock(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    formats = {
        'html': 'HTML',
        'xml': 'XML',
        'php': 'PHP',
        'yaml': 'YAML',
        'jinja': 'Jinja',
        'html+jinja': 'HTML',
        'jinja+html': 'Jinja',
        'twig': 'Twig',
        'html+twig': 'HTML',
        'twig+html': 'Twig',
        'php+html': 'PHP',
        'html+php': 'HTML',
        'ini': 'INI',
        'php-annotations': 'Annotations',
        'php-standalone': 'Standalone Use',
        'php-symfony': 'Framework Use',

        # http://pygments.org/docs/lexers/#lexers-for-css-and-related-stylesheet-formats
        'css': 'CSS',
        'less': 'LESS',
        'sass': 'SASS',
        'scss': 'SCSS',

        # http://pygments.org/docs/lexers/#pygments.lexers.shell.BashLexer
        'bash': 'Bash',

        # http://pygments.org/docs/lexers/#pygments.lexers.objective.SwiftLexer
        'swift': 'Swift',

        # http://pygments.org/docs/lexers/#lexers-for-objective-c-family-languages
        'objective-c': 'Objective C',
        'objectivec': 'Objective C',
        'objc': 'Objective C',
        'obj-c': 'Objective C',

        # http://pygments.org/docs/lexers/#pygments.lexers.markup.RstLexer
        'rest': 'reST',

        # http://pygments.org/docs/lexers/#pygments.lexers.javascript.JavascriptLexer
        'js': 'JS',
        'javascript': 'Javascript',
        'coffee-script': 'CoffeeScript',
        'coffeescript': 'CoffeeScript',
        'coffee': 'CoffeeScript',

        # http://pygments.org/docs/lexers/#pygments.lexers.data.JsonLexer
        'json': 'JSON',

        # http://pygments.org/docs/lexers/#lexers-for-python-and-related-languages
        'python': 'Python',
        'py': 'Python',
        'sage': 'Python',
        'pycon': 'Python Console',
        'python3': 'Python3',
        'py3': 'Python3',
        'numpy': 'NumPy',

        # http://pygments.org/docs/lexers/#pygments-lexers-for-jvm-languages
        'java': 'Java',
        'groovy': 'Groovy',
        'scala': 'Scala',
    }

    def __init__(self, *args):
        Directive.__init__(self, *args)
        env = self.state.document.settings.env
        config_block = env.app.config.config_block

        for language in config_block:
            self.formats[language] = config_block[language]

    def run(self):
        env = self.state.document.settings.env

        node = nodes.Element()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)

        entries = []
        error_node = nodes.error()

        for i, child in enumerate(node):
            if isinstance(child, nodes.literal_block):
                if 'language' in child:
                    language = child['language']
                else:
                    language = env.app.config.highlight_language

                innernode = nodes.emphasis(self.formats[language],
                                           self.formats[language])

                para = nodes.paragraph()
                para += [innernode, child]

                entry = nodes.list_item('')
                entry.append(para)
                entries.append(entry)
            elif isinstance(child, nodes.system_message):
                error_node += child.children

        if error_node.children:
            return [error_node]

        resultnode = configurationblock()
        resultnode.append(nodes.bullet_list('', *entries))

        return [resultnode]


def visit_configurationblock_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='configuration-block'))


def depart_configurationblock_html(self, node):
    self.body.append('</div>\n')


def visit_configurationblock_latex(self, node):  # pragma: no cover
    pass


def depart_configurationblock_latex(self, node):  # pragma: no cover
    pass


def setup(app):
    app.add_config_value('config_block', {}, 'env')
    app.add_node(
        configurationblock,
        html=(visit_configurationblock_html, depart_configurationblock_html),
        latex=(visit_configurationblock_latex,
               depart_configurationblock_latex))
    app.add_directive('configuration-block', ConfigurationBlock)
