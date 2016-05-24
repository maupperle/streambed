#! /usr/bin/env python

""" Examples of streambed capabilites

Example data is from the Little River, a tributary of the Cape Fear River in
North Carolina, USA.
"""

import os
import sys

# import streambed library
os.chdir("..")
root = os.getcwd()
sys.path.append(root + '/streambed')
import streambed as sb

# Set parameters using default values
parameters = sb.Parameters(root + '/exampleData/')
print(parameters.sedimentDensity)

# Calculate cross-sectional at a site along the river
xs = sb.CrossSection(parameters.dataDirectory + 'NiagaraCarthrage-78.xsection')
print('cross sectional area = ' + str(xs.area))

# Initialize channel
channel = sb.Channel(parameters.dataDirectory + 'LittleRiver.channel')
print(channel.elevation)