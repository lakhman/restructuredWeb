# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ConfigurationBlockTest(BaseTest):
    def test_basic(self):
        """
        Test default multiple config block
        """
        self.do_component_fixture_test_with_real_sphinx('configurationblock', 'basic')

    def test_default_lang(self):
        """
        Test default language is used from config
        """
        self.do_component_fixture_test_with_real_sphinx('configurationblock', 'default-lang', confoverrides={'highlight_language': 'php'})

    def test_error(self):
        """
        Test error is thrown is no argument
        """
        self.do_component_fixture_test_with_real_sphinx('configurationblock', 'error')
