#! /usr/bin/env python

import os
import sys

os.path.abspath(os.getcwd())
os.chdir("..")
root = os.getcwd()
sys.path.append(root + '/streambed')
import streambed as sb

dataDir = root + '/exampleData/'

xs = sb.CrossSection(dataDir + 'NiagaraCarthrage-78.xsection')
print(xs.area)
