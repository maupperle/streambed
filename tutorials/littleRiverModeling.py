#! /usr/bin/env python

""" Examples of streambed capabilites

Example data is from the Little River, a tributary of the Cape Fear River in
North Carolina, USA.
"""

import os
import streambed as sb

# Initialize model with default parameters
model = sb.Model(os.getcwd() + '/exampleData/')

# Calculate cross-sectional at a site along the river
xs = sb.CrossSection(model.domain['NiagaraCarthrage-78'])
xs.plot()
print('cross sectional area = ' + str(xs.area))

# Initialize channel
channel = sb.Channel(model.domain['LittleRiver'])
channel.plot()
<<<<<<< HEAD

# Calibrate drainage area-discharge relationship
dataDictionary = sb.get_calibration_data(model.domain['SandhillsGages'])

# Estimate discharge along stream

=======
channel.findQ()
>>>>>>> ad650696ac42685344883ed1231c762ef113602a
