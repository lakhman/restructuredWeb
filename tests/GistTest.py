# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class GistTest(BaseTest):
    def test_gist_script(self):
        """
        Test a gist script embed
        """
        self.do_component_fixture_test('gist', 'gist-script')

    def test_gist_url(self):
        """
        Test a gist script embed
        """
        self.do_component_fixture_test('gist', 'gist-url')

    def test_gist_valid_url(self):
        """
        Test a valid gist url - no modification required
        """
        self.do_component_fixture_test('gist', 'gist-valid-url')

    def test_gist_invalid_url(self):
        """
        Test a invalid gist url should throw an error
        """
        self.do_component_fixture_test('gist', 'gist-invalid-url')

    def test_gist_invalid_url_blank(self):
        """
        Test a blank invalid gist url should throw an error
        """
        self.do_component_fixture_test('gist', 'gist-invalid-url-blank')
