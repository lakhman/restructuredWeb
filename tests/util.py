#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
import logging
import os
import sys
import docutils

from sphinx_testing.path import path
from sphinx_testing import with_app as with_sphinx_testing

test_apps = path(__file__).parent.joinpath('testapps').abspath()

rootdir = path(os.path.dirname(__file__) or '.').abspath()
tempdir = path('./.cache').abspath()

# log = logging.getLogger("bootstrap.logger")
# log.debug("Debug : %s", app.builddir)
logging.basicConfig(stream=sys.stderr)
logging.getLogger("bootstrap.logger").setLevel(logging.DEBUG)


# Utils -----------------------------------------------------------------------


def with_app(*args, **kwargs):  # pragma: no cover
    """Decorator for passing a test Sphinx app to a function.
    Extends sphinx_testing's version by defaulting to a base test directory
    if none is specified. The test directory will be copied to a temporary
    directory before calling the function.

    https://github.com/nyergler/hieroglyph/blob/master/src/hieroglyph/tests/util.py
    """

    if 'buildername' not in kwargs:
        kwargs['buildername'] = 'html'

    if 'copy_srcdir_to_tmpdir' not in kwargs:
        kwargs['copy_srcdir_to_tmpdir'] = True

    if 'srcdir' not in kwargs and 'testapp' in kwargs:
        kwargs['srcdir'] = test_apps + '/' + kwargs['testapp']
        kwargs.__delitem__('testapp')

    return with_sphinx_testing(*args, **kwargs)


def make_document(source_name, contents):
    """
    Parse ```contents``` into a docutils document.

    https://github.com/nyergler/hieroglyph/blob/master/src/hieroglyph/tests/util.py
    """

    parser = docutils.parsers.rst.Parser()
    document = docutils.utils.new_document(
        source_name,
        docutils.frontend.OptionParser(
            components=(
                docutils.parsers.rst.Parser,
                docutils.writers.html4css1.Writer,
            ),
        ).get_default_values(),
    )

    # This stops the error output in the test
    # Set it to 3 to view the failed output
    document.reporter.report_level = 4
    parser.parse(contents, document)

    return document
