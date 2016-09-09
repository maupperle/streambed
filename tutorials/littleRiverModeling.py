#! /usr/bin/env python

""" Examples of streambed capabilites
Example data is from the Little River, a tributary of the Cape Fear River in
North Carolina, USA.
"""
import sys
sys.path.append("C:\Users\Matthew\Documents\Streambed_Mapping\streambed")

import os
import streambed as sb

# Initialize model with default parameters. Domains are printed when initializing.
model = sb.Model(os.getcwd() + '/exampleData/')

# Calculate cross-sectional area at a site along the river
xs = sb.CrossSection(model.domain['NiagaraCarthrage-78'])
xs.plot()
print('cross sectional area = ' + str(xs.area))

# Initialize channel
channel = sb.Channel(model.domain['LittleRiver'])

# Estimate discharge along a channel using calibration data
channel.findQ(model.domain['SandhillsGages'])



# Plot longitudinal parameters
channel.plot()

# Model streambed grain size along the length of the channel
channel.predict_bed_grain_size(model.parameters)