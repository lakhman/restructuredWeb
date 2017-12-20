# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class LayoutTest(BaseTest):
    def test_layout_switch(self):
        """
        Test layout switch
        """
        self.do_component_fixture_test_with_real_sphinx('layout', 'layout')

    def test_layout_multiple(self):
        """
        Test multiple layout directives throw an error
        """
        self.do_component_fixture_test_with_real_sphinx('layout', 'multiple-error')
