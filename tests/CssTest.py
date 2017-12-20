# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class CssTest(BaseTest):
    def test_basic_css(self):
        """
        Test basic output of css
        """
        self.do_component_fixture_test_with_real_sphinx('css', 'basic-css')
