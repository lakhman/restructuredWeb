# -*- encoding: utf-8 -*-
import unittest2 as unittest
from unittest import TestCase

from .AdsenseTest import AdsenseTest
from .CodepenTest import CodepenTest
from .ConfigurationBlockTest import ConfigurationBlockTest
from .CssTest import CssTest
from .GistTest import GistTest
from .JavascriptTest import JavascriptTest
from .JSFiddleTest import JSFiddleTest
from .LayoutTest import LayoutTest
from .TedTest import TedTest
from .TwitterTest import TwitterTest
from .YoutubeTest import YoutubeTest

TestCase.maxDiff = None
unittest.util._MAX_LENGTH = 10000

# -------------------------------------------------------------------------------------------------
# Generated test suite, find all tests from these modules and run them
#
# To run this with PyCharm use the following test configuration
#
# Path: /path/to/project/sphinx-bootstrap/src/tests/generated_suite.py
# Working Directory: /path/to/project/sphinx-bootstrap/tests
#
# With tox:
# tox -e py27
# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AdsenseTest))
    test_suite.addTest(unittest.makeSuite(CodepenTest))
    test_suite.addTest(unittest.makeSuite(ConfigurationBlockTest))
    test_suite.addTest(unittest.makeSuite(CssTest))
    test_suite.addTest(unittest.makeSuite(GistTest))
    test_suite.addTest(unittest.makeSuite(JavascriptTest))
    test_suite.addTest(unittest.makeSuite(JSFiddleTest))
    test_suite.addTest(unittest.makeSuite(LayoutTest))
    test_suite.addTest(unittest.makeSuite(TedTest))
    test_suite.addTest(unittest.makeSuite(TwitterTest))
    test_suite.addTest(unittest.makeSuite(YoutubeTest))

    runner = unittest.TextTestRunner()
    runner.run(test_suite)
