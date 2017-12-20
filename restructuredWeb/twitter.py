#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
import re


class twitter_tweet_quote(nodes.General, nodes.Element):
    pass


def visit_twitter_tweet(self, node):
    atts = {
        'class': " ".join(node['classes']),
        'data-id': node['tweet-id'],
        'data-lang': node['lang'],
    }

    if 'cards' in node:
        atts['data-cards'] = node['cards']

    if 'conversation' in node:
        atts['data-conversation'] = node['conversation']

    if 'link-color' in node:
        atts['data-link-color'] = node['link-color']

    if 'width' in node:
        atts['data-width'] = node['width']

    if 'dnt' in node:
        atts['data-dnt'] = 'true'

    if node['theme'] != 'light':
        atts['data-theme'] = node['theme']

    self.body.append(self.starttag(node, 'blockquote', **atts))

    format_attr = {
        'tweet_url': node['tweet-url'],
        'tweet_handle': '@' + node['tweet-handle'],
    }

    # error - mobile redirects dont work - you need the actual full url
    link = '<a href="{tweet_url}">{tweet_handle}</a>'.format(**format_attr)
    self.body.append('<p lang="en" dir="ltr">{text}</p> {link}'.format(
        link=link, text=node['text']))
    self.body.append('</blockquote>\n')
    self.body.append('<div class="clearfix"></div>\n'
                     )  # Twitter floats the element when aligning

    raise nodes.SkipNode


def align(argument):
    align_h_values = ('left', 'center', 'right')
    return directives.choice(argument, align_h_values)


def lang_choice(argument):
    # https://dev.twitter.com/web/overview/languages
    twitter_lang_dict = []
    twitter_lang_dict += [
        'en', 'ar', 'bn', 'cs', 'da', 'de', 'el', 'es', 'fa', 'fi', 'fil'
    ]
    twitter_lang_dict += [
        'fr', 'he', 'hi', 'hu', 'id', 'it', 'ja', 'ko', 'msa', 'nl', 'no'
    ]
    twitter_lang_dict += [
        'pl', 'pt', 'ro', 'ru', 'sv', 'th', 'tr', 'uk', 'ur', 'vi', 'zh-cn'
    ]
    twitter_lang_dict += ['zh-tw']

    return directives.choice(argument, twitter_lang_dict)


class TwitterTweet(Directive):
    optional_arguments = 1
    has_content = False
    final_argument_whitespace = False

    # https://dev.twitter.com/web/embedded-tweets/parameters
    option_spec = {
        'text': directives.unchanged,
        'class': directives.class_option,
        'name': directives.unchanged,
        'dark': directives.flag,
        'link-color': directives.unchanged,
        'lang': lang_choice,
        'cards': directives.unchanged,
        'conversation': directives.unchanged,
        'dnt': directives.flag,
        'width': directives.positive_int,
        'align': align,
    }

    def run(self):
        url_tpl = 'https://twitter.com/{tweet_handle}/status/{tweet_id}'
        tweet_handle = None
        tweet_id = None
        url_regex = r"^(?:https?:\/\/twitter\.com)?\/?(?:#!\/)?(\w+)" \
                    r"(?:\/status(?:es)?)?\/(\d+)$"
        try:
            if self.arguments:
                url_match = re.match(url_regex, self.arguments[0])
                if url_match:
                    tweet_handle = url_match.group(1)
                    tweet_id = url_match.group(2)
                else:
                    raise ValueError()
        except ValueError:
            val_error = 'Invalid id attribute value for "%s" directive: "%s".'
            raise self.error(val_error % (self.name, self.arguments[0]))

        if tweet_id is None or tweet_handle is None:
            raise self.error(
                '..twitter-tweet must have a {handle}/{ID}'
                ' e.g: ..twitter-tweet: elonmusk/902087339010211840.')

        node = twitter_tweet_quote('', **self.options)
        node['classes'] = ['twitter-tweet']
        node['classes'] += self.options.get('class', [])
        node['lang'] = self.options.get('lang', 'en')
        node['tweet-id'] = tweet_id
        node['tweet-handle'] = tweet_handle
        node['tweet-url'] = url_tpl.format(
            tweet_handle=tweet_handle, tweet_id=tweet_id)
        node['text'] = self.options.get('text', node['tweet-url'])
        node['theme'] = 'dark' if 'dark' in self.options else 'light'

        if 'cards' in self.options:
            node['cards'] = self.options['cards']

        if 'conversation' in self.options:
            node['conversation'] = self.options['conversation']

        if 'link-color' in self.options:
            node['link-color'] = self.options['link-color']

        if 'dnt' in self.options:
            node['dnt'] = self.options['dnt']

        if 'width' in self.options:
            node['width'] = self.options['width']

        if 'align' in self.options:
            node['classes'] += ['tw-align-%s' % self.options['align']]
        else:
            node['classes'] += ['tw-align-center']

        self.add_name(node)
        return [node]


def setup(app):
    app.add_node(twitter_tweet_quote, html=(visit_twitter_tweet, None))
    app.add_directive('twitter-tweet', TwitterTweet)
