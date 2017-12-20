# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class JavascriptTest(BaseTest):
    def test_basic_script(self):
        """
        Test we can insert javascript raw at the current point
        """
        self.do_component_fixture_test_with_real_sphinx('javascript', 'basic-script')

    def test_dom_ready(self):
        """
        Test inline option, leave the node as it and write it
        """
        self.do_component_fixture_test_with_real_sphinx('javascript', 'inline')
