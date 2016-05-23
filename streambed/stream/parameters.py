#! /usr/bin/env python

class Parameters(object):
    
    self.waterDensity = 1000
    self.gravitationalAcceleration = 9.81    
    
    def __init__(self, sedimentDensity=2650):
        self.sedimentDensity = sedimentDensity
