#! /usr/bin/env python

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt


class Channel(object):
    calibration = [[4.739678e+008, 37.4], [9.013159e+008, 75.8], 
                   [2.411279e+008, 17.6], [4.739678e+008, 37.4], 
                   [9.013159e+008, 75.8]]
    
    """ Data structure and methods for stream channels.
    
    Parameters are stored in points along the stream. Parameter values are
    initialized from a .channel data file.
    """
    
    def __init__(self, filePath):
        """ Initialize channel object using values from a .channel data file.
        
        Parameters
        ----------
        filePath : string
            Full file path to .channel data file.  
        
        """

        data = np.genfromtxt(filePath, dtype=None, delimiter=',', names=True)
        self.x = data['x']
        self.y = data['y']
        self.elevation = data['elevation']
        self.drainageArea = data['drainageArea']
        self.distanceFromMouth = data['distanceFromMouth']
        self.slope = self.slope(self.distanceFromMouth, self.elevation)
        self.calibration = [[4.739678e+008, 37.4], [9.013159e+008, 75.8], 
                            [2.411279e+008, 17.6], [4.739678e+008, 37.4], 
                            [9.013159e+008, 75.8]]

    def slope(self, x, z):
        """ Calculate channel slope along a stream.
        
        Slope is calculated using a central-differencing window except at
        channel endpoints where slope is calculated using the adjacent point.
        
        Parameters
        ----------
        x : array
            Distance at each point along the channel.
        z : array
            Elevation at each point along the channel.
            
        Returns
        -------
        slope : array
            Slope (percent) at each point along the channel.
            
            
        """

        lx = len(x)
        
        slope = []
       
        slope.append((z[1] - z[0]) / (x[1] - x[0]))

        for i in range(1, lx - 1):
            slope.append((z[i + 1] - z[i - 1]) / (x[i + 1] - x[i - 1]))
        
        slope.append((z[lx - 1] - z[lx - 2]) / (x[lx - 1] - x[lx - 2]))
        
        return slope
    
    def findQ(self):
        """ Calculate the the predicted bankful flow from the drainage area.
        Based on the equation Q = K*A^c where:
        Q = Flowrate
        A = Drainage Area
        K,c = constants
        
        Parameters
        ------------        
        calibSet: The equation will be calibrated based on known data inputted 
                  from the calibSet argument in the form of a list of lists
                  in the format [[A,Q],...]
        self.drainageArea: This will be used to input the drainage area of the 
                           of the fluvial region in question. 
        
        Creates a plot of Drainage Area by Flowrate based on the calibrated 
        equation.
        """
        
        "convert eqation of form Q=kA^c to log(Q)=log(k)+c*log(A)"
        logA = [np.log10(coord[0]) for coord in self.calibration]
        logQ = [np.log10(coord[1]) for coord in self.calibration]
        coefs = poly.polyfit(logA, logQ, 1) 
        "coeffecients are in the form of [log10(K), c]"
        K = 10**coefs[0]
        c = coefs[1]
        estimQ = [K*(Area**c) for Area in self.drainageArea]
        
        plt.figure()
        plt.plot(self.drainageArea, estimQ, 'k')
        plt.xlabel('Drainage Area')
        plt.ylable('Estimated Flow Rate')
        
        plt.show()
        
    
    def plot(self):
        """ Plot channel map and longitudinal profile parameters. 
        
        """        
        
        plt.figure()
        plt.plot(self.x, self.y, 'k')
        plt.xlabel('easting')
        plt.ylabel('northing')
        plt.gca().set_aspect('equal', adjustable='box')
        
        plt.figure()
        
        plt.subplot(3, 1, 1)
        plt.plot(self.distanceFromMouth, self.elevation, 'k')
        plt.xlabel('distance from mouth')
        plt.ylabel('elevation')
        
        plt.subplot(3, 1, 2)
        plt.plot(self.distanceFromMouth, self.slope, 'k')
        plt.xlabel('distance from mouth')
        plt.ylabel('slope')

        plt.subplot(3, 1, 3)
        plt.plot(self.distanceFromMouth, self.drainageArea, 'k+')
        plt.xlabel('distance from mouth')
        plt.ylabel('drainage area')
                
        plt.show()
    