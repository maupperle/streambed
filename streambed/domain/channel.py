#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class Channel(object):
    
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
    