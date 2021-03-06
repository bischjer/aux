# -*- coding: utf-8 -*-

"""
    based on flask.ext
    ~~~~~~~~~

    Redirect imports for extensions.  This module basically makes it possible
    for us to transition from flaskext.foo to flask_foo without having to
    force all extensions to upgrade at the same time.

    When a user does ``from flask.ext.foo import bar`` it will attempt to
    import ``from flask_foo import bar`` first and when that fails it will
    try to import ``from flaskext.foo import bar``.

    We're switching from namespace packages because it was just too painful for
    everybody involved.

    :copyright: (c) 2011 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import sys

def setup():
    from aux.internals.pluginhook import PluginImporter
    importer = PluginImporter(['aux_service_%s'], __name__)
    importer.install()

setup()
del setup

