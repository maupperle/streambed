#! /usr/bin/env python

import numpy as np

class Channel(object):
    
    def __init__(self, filePath):

        data = np.genfromtxt(filePath, dtype=None, delimiter=',', names=True)
        self.x = data['x']
        self.y = data['y']
        self.elevation = data['elevation']
        self.distanceFromMouth = data['distanceFromMouth']
        self.distanceFromDivide = data['distanceFromDivide']
        self.sampleDistance = data['sampleDistance']
