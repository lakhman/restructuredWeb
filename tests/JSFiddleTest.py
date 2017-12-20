# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class JSFiddleTest(BaseTest):
    def test_class_wrap(self):
        """
        Test a simple jsfiddle is outputted
        """
        self.do_component_fixture_test('jsfiddle', 'basic')

    def test_height(self):
        """
        Test height is added to iframe
        """
        self.do_component_fixture_test('jsfiddle', 'height')
