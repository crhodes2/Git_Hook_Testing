# !/usr/bin/env python3
# -*- mode: python -*-
###############################################################
'''
                         About program

'''
####################### List of modules #######################

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from subprocess import Popen, PIPE

import os               # for the operating system
import re               # for regular expressions
import subprocess       # for os sub processes
import sys              # for system

#######################    Variables    #######################

globe = "global"            # a global variable
fantastic = "fantastique"     # another global variable

#######################    Functions    #######################

def function():
    print('step1')
    print('step2')
    print('step3')
    print('step4')
    print('step5')
    print('step6')

def a_function(par):
    print('a function with a {0} variable'. format(par))

def main():
    local = "local"       # a local variable
    print(function())
    print(a_function(local))  # calling a function with a local variable
    print(a_function(globe)) # calling a function with a global variable
    print(a_function(fantastic)) # calling a function with another global variable


#######################       Main      #######################

if __name__ == "__main__":
    main()