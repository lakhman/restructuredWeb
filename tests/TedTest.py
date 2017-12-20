# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class TedTest(BaseTest):
    def test_basic(self):
        """
        Test youtube simple iframe embed
        """
        self.do_component_fixture_test('ted', 'basic')

    def test_4by3(self):
        """
        Test 4by3 class
        """
        self.do_component_fixture_test('ted', '4by3')

    def test_no_arg(self):
        """
        Test no arg
        """
        self.do_component_fixture_test('ted', 'no-arg')
