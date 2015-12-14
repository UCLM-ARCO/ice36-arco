#!/usr/bin/env python
# -*- mode: python; coding: utf-8 -*-

import os
from distutils.core import setup

PWD = os.path.abspath(os.path.dirname(__file__))
ICE_DIR = os.path.join(PWD, "../src")
PACKAGE_DIR = os.path.join(ICE_DIR, 'python/python')

modules = []
for f in os.listdir(PACKAGE_DIR):
    if f.endswith(".py"):
        modules.append(f[:-3])

setup(
    name = 'zeroc-ice36',
    version = '3.6.1',
    description = 'The Internet Communications Engine',
    author = 'ZeroC, Inc.',
    author_email = 'support@zeroc.com',
    url = 'https://zeroc.com',

    package_dir = {'': PACKAGE_DIR},
    py_modules = modules, 
    packages = ["IceBox", "IceGrid", "IceMX", "IcePatch2", "IceStorm"],

    # FIXME: not valid for other than Debian Jessie
    data_files = [('lib/python2.7/dist-packages/', [os.path.join(PACKAGE_DIR, 'IcePy.so.3.6.1')])],
)
