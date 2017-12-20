# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class YoutubeTest(BaseTest):
    def test_youtube_simple(self):
        """
        Test youtube simple iframe embed
        """
        self.do_component_fixture_test('youtube', 'youtube-simple')

    def test_youtube_class(self):
        """
        Test youtube simple class
        """
        self.do_component_fixture_test('youtube', 'youtube-class')

    def test_youtube_no_id(self):
        """
        Test youtube no id error
        """
        self.do_component_fixture_test('youtube', 'youtube-no-id')

    def test_youtube_invalid_id(self):
        """
        Test youtube invalid id error
        """
        self.do_component_fixture_test('youtube', 'youtube-invalid-id')

    def test_youtube_4by3(self):
        """
        Test youtube 4by3 responsive class
        """
        self.do_component_fixture_test('youtube', 'youtube-4by3')

    def test_youtube_autoplay(self):
        """
        Test youtube autoplay url
        """
        self.do_component_fixture_test('youtube', 'youtube-url-autoplay')

    def test_youtube_list_type(self):
        """
        Test youtube listTypes can have no id and listtype is replaced is listType
        """
        self.do_component_fixture_test('youtube', 'youtube-no-id-listType')

    def test_youtube_all_params(self):
        """
        Test youtube autoplay all params
        """
        self.do_component_fixture_test('youtube', 'youtube-url-all-params')
