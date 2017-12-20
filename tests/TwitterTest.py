# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class TwitterTest(BaseTest):
    def test_simple_tweet(self):
        """
        Test simple basic tweet with id as option
        """
        self.do_component_fixture_test('twitter', 'simple-tweet')

    def test_simple_tweet_short_url(self):
        """
        Test simple basic tweet with a shorthand url - we use regex to parse the handle/id
        elonmusk/899682569951760384
        """
        self.do_component_fixture_test('twitter', 'simple-tweet-full-url')


    def test_simple_tweet_full_url(self):
        """
        Test simple basic tweet with a full url - we use regex to parse the handle/id
        https://twitter.com/elonmusk/status/899682569951760384
        https://twitter.com/elonmusk/statuses/899682569951760384
        """
        self.do_component_fixture_test('twitter', 'simple-tweet-full-url')

    def test_tweet_placeholder_text(self):
        """
        Test text placeholder with option :text:
        """
        self.do_component_fixture_test('twitter', 'tweet-text')

    def test_tweet_argument_error(self):
        """
        Test Tweet with error argument
        """
        self.do_component_fixture_test('twitter', 'tweet-argument-error')

    def test_tweet_no_id(self):
        """
        Test Tweet with no id - error should be thrown
        """
        self.do_component_fixture_test('twitter', 'tweet-no-id')

    def test_tweet_theme(self):
        """
        Test Tweet theme via :dark: flag
        """
        self.do_component_fixture_test('twitter', 'tweet-theme')

    def test_tweet_link_color(self):
        """
        Test link color attr can be added
        """
        self.do_component_fixture_test('twitter', 'tweet-link-color')

    def test_tweet_align(self):
        """
        Test tweet align can be set
        """
        self.do_component_fixture_test('twitter', 'tweet-align')

    def test_tweet_lang(self):
        """
        Test tweet lang can be set
        """
        self.do_component_fixture_test('twitter', 'tweet-lang')

    def test_tweet_cards(self):
        """
        Test tweet cards can be set
        """
        self.do_component_fixture_test('twitter', 'tweet-cards')

    def test_tweet_conversation(self):
        """
        Test tweet conversation can be set
        """
        self.do_component_fixture_test('twitter', 'tweet-conversation')

    def test_tweet_dnt(self):
        """
        Test tweet dnt can be set
        """
        self.do_component_fixture_test('twitter', 'tweet-dnt')

    def test_tweet_width(self):
        """
        Test tweet width can be set
        """
        self.do_component_fixture_test('twitter', 'tweet-width')
