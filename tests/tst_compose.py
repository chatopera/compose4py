#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright 2020 (c) Scrapy developers. All rights reserved.
# https://github.com/scrapy/scrapy/blob/master/LICENSE
# Modifications copyright (C) 2020 Chatopera Inc, <https://www.chatopera.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Author: Hai Liang Wang
# Date: 2020-03-21:10:16:05
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2020-03-21:10:07:36"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.pardir))

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

# Get ENV
ENVIRON = os.environ.copy()

from compose4py import Compose

import unittest

def mw_1(ctx, loader_context):
    print("mw_1: %s" % ctx)
    print("mw_1 loader_context: %s" % loader_context)
    ctx += ":mw1"
    ctx = yield ctx
    ctx += ":post_mw1"
    return ctx

def mw_2(ctx):
    print("mw_2: %s" % ctx)
    ctx += ":mw2"
    ctx = yield ctx
    ctx += ":post_mw2"
    return ctx

def mw_3(ctx):
    print("mw_3: %s" % ctx)
    ctx += ":mw3"
    return ctx

# run testcase: python /Users/hain/git/compose4py/tests/tst_compose.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_map_compose(self):
        logging.info("test_map_compose")
        compose = Compose(mw_1, mw_2, mw_3, loader_context = {"foo": "bar"})
        v = compose("foo")
        print("final: %s" % v)


def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_map_compose"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main(argv):
    test()

if __name__ == '__main__':
    # /Users/hain/git/compose4py/tests/tst_compose.py --verbosity 1 # DEBUG 1; INFO 0; WARNING -1
    app.run(main)
