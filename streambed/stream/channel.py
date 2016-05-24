#! /usr/bin/env python

import numpy as np

class Channel(object):
    
    """ Data structure and methods for stream channels.
    
    Parameters are stored in points along the stream. Parameter values are
    initialized from a .channel data file.
    """
    
    def __init__(self, filePath):

        data = np.genfromtxt(filePath, dtype=None, delimiter=',', names=True)
        self.x = data['x']
        self.y = data['y']
        self.elevation = data['elevation']
        self.drainageArea = data['drainageArea']
        self.distanceFromMouth = data['distanceFromMouth']
