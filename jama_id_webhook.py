#!/usr/bin/env python3
# -*- mode: python -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from subprocess import Popen, PIPE

import os
import sys

def function():
    print('step1')
    print('step2')
    print('step3')
    print('step4')
    print('step5')
    print('step6')

argu = "typical"

def a_function(arg):
    print('a {0} function'. format(arg))

if __name__ == "__main__":
    print(function())
    print(a_function(argu))
