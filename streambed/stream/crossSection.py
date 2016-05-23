#! /usr/bin/env python
""" Channel cross-section methods """

import numpy as np

class CrossSection(object):
    
    def __init__(self, filePath):

        """ header """
        with open(filePath, 'r') as fp:
            header = fp.read()
        rows = header.split('\n')
        
        self.siteName = rows[0]
        self.date = rows[1]
        self.coordinates = rows[2]

        """ data """
        data = np.genfromtxt(filePath, dtype=None, delimiter=',', skip_header=3, names=['x', 'depth'])
        x = data['x']
        depth = data['depth']

        self.area = np.trapz(depth, x=x)
