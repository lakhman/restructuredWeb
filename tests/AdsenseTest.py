# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class AdsenseTest(BaseTest):
    def test_class_wrap(self):
        """
        Test ad is wrapped in a div if a class is provided
        """
        self.do_component_fixture_test_with_real_sphinx('adsense', 'class-wrap')

    def test_client_id(self):
        """
        Test the client id is rendered
        """
        self.do_component_fixture_test_with_real_sphinx('adsense', 'client-id')

    def test_invalid_client_id(self):
        """
        Test invalid client id
        """
        self.do_component_fixture_test_with_real_sphinx('adsense', 'invalid-client-id',
                                                        confoverrides={'adsense_client_id': ''})
    def test_invalid_client_adslot(self):
        """
        Test invalid client adslot
        """
        self.do_component_fixture_test_with_real_sphinx('adsense', 'invalid-client-adslot')

    def test_default_slot(self):
        """
        Test the default slot is rendered if no argument is passed
        """
        self.do_component_fixture_test_with_real_sphinx('adsense', 'default-slot')

    def test_named_slot(self):
        """
        Test our named slot is rendered if passed as an argument
        """
        self.do_component_fixture_test_with_real_sphinx('adsense', 'named-slot')
