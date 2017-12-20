#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
import codecs
import glob
import os
from unittest import TestCase

import unittest2 as unittest
from sphinx.writers.html import HTMLTranslator
from sphinx_testing import TestApp
from nose.tools import nottest

from .util import make_document, test_apps

path = os.path.dirname(os.path.realpath(__file__))

TestCase.maxDiff = None
unittest.util._MAX_LENGTH = 10000


class BaseTest(unittest.TestCase):
    maxDiff = None
    app = None

    @classmethod
    def setUpClass(cls):
        # We use the builder from this to manually parse our rest to make our tests faster
        cls.app = TestApp(
            buildername='html',
            copy_srcdir_to_tmpdir=True,
            srcdir=test_apps + '/html',
            confoverrides={'master_doc': 'index'},
        )
        cls.app.build()

    def parse_rest_document(self, rst_src):
        """
        Parse our rest document and return a joined body

        :return string:
        """
        document = make_document('testing', rst_src)
        translator = HTMLTranslator(self.app.builder, document)
        document.walkabout(translator)

        return u''.join(x for x in translator.body).strip().replace("'", "\\'")

    def load_component_fixture(self, component, fixture):
        """
        Load our component fixtures from disk and return them in a zipped list

        :param component: e.g: alert, button
        :param fixture: e.g: alert-classes, button-default
        :return:
        """
        fixtures = glob.glob("{0}/fixtures/{1}/{2}.rst".format(path, component, fixture))
        expected = glob.glob("{0}/fixtures/{1}/{2}.html".format(path, component, fixture))

        zipped = list(zip(fixtures, expected))
        if len(zipped) == 0:  # pragma: no cover
            self.fail("fixture {0}/{1} was not found".format(component, fixture))

        return zipped

    @nottest
    def do_component_fixture_test(self, component, fixture, msg=None):
        """
        Read our test (restructuredText) and control (HTML) from disk and assert them
        This is much faster as we don't boot sphinx but do it manually, but these tests
        don't work with sphinx events.
        :param component: e.g: alert, button
        :param fixture: e.g: alert-classes, button-default
        :param msg: Optional Message
        :return:
        """
        zipped = self.load_component_fixture(component, fixture)

        for rst, html in zipped:
            with codecs.open(rst, "r", "utf-8") as r:
                with codecs.open(html, "r", "utf-8") as h:
                    rst_src = r.read()
                    html_src = h.read()

                    actual = self.parse_rest_document(rst_src)
                    expected = html_src.strip().replace("'", "\\'")

                    self.assertMultiLineEqual(expected, actual, msg)

    @nottest
    def do_component_fixture_test_with_real_sphinx(self, component, fixture, msg=None, confoverrides={}):
        """
        This parses our test file through real sphinx (testapps/html) which is a blank layout
        This is much slower then doing it via our translator, but needed for some tests like
        font awesome which hook into the sphinx events to manipulate the dom at various cycles

        :param component: e.g: alert, button
        :param fixture: e.g: alert-classes, button-default
        :param msg: Optional Message
        :return:
        """
        zipped = self.load_component_fixture(component, fixture)

        for rst, html in zipped:
            with codecs.open(rst, "r", "utf-8") as r:
                with codecs.open(html, "r", "utf-8") as h:
                    # rst_src = r.read()
                    html_src = h.read()
                    conf_dir = test_apps + '/html'
                    src_dir = os.path.dirname(rst)
                    conf_overrides = {'master_doc': fixture, 'templates_path': ['_templates']}
                    conf_overrides.update(confoverrides)

                    self.app = TestApp(
                        buildername='html',
                        copy_srcdir_to_tmpdir=True,
                        srcdir=src_dir,
                        confoverrides=conf_overrides,
                        confdir=conf_dir)
                    # we need to delete all other rst files copied, else it runs them as well
                    file_list = os.listdir(self.app.srcdir)
                    exclude_files = ['_build', fixture + '.rst']
                    for file in file_list:
                        if file not in exclude_files:
                            os.unlink(self.app.srcdir + os.sep + file)
                    self.app.build()
                    html = (self.app.outdir / fixture + '.html')

                    with codecs.open(html, "r", "utf-8") as b:
                        actual = b.read().strip()

                    expected = html_src.strip()

                    self.assertMultiLineEqual(expected, actual, msg)
