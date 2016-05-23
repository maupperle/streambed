#! /usr/bin/env python

import os
import sys

os.chdir("..")
root = os.getcwd()
sys.path.append(root + '/streambed')
import streambed as sb

parameters = sb.Parameters(root + '/exampleData/')
print(parameters.sedimentDensity)

xs = sb.CrossSection(parameters.dataDirectory + 'NiagaraCarthrage-78.xsection')
print('cross sectional area = ' + str(xs.area))

chan = sb.Channel(parameters.dataDirectory + 'LittleRiver.channel')
print(chan.elevation)