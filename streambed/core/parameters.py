#! /usr/bin/env python

class Parameters(object):
    
    """ Data structure and methods for parameters of a streambed model.
    """    
    
    waterDensity = 1000
    gravitationalAcceleration = 9.81
    
    def __init__(self, dataDirectory, sedimentDensity=2650):

        self.dataDirectory = dataDirectory
        self.sedimentDensity = sedimentDensity
        