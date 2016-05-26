#! /usr/bin/env python

class Parameters(object):
    
    """ Data structure and methods for parameters of a streambed model.
    """    

    def __init__(self, sedimentDensity=2650):
        self.waterDensity = 1000
        self.gravitationalAcceleration = 9.81
        self.manningsn = 0.07
        self.criticalShearStress = 0.0067
        self.sedimentDensity = sedimentDensity
        
        self.print_attributes()
        
    def print_attributes(self):
        print('Parameter values:\n')      
        
        for key in self.__dict__.keys():
            print('%s = %s' % (key, self.__dict__[key]))
            
        print('\n----------------------------')