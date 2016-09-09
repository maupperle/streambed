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
        slope : numpy array
            Slope (percent) at each point along the channel.
                
        """

        lx = len(x)
        
        slope = []
       
        slope.append((z[1] - z[0]) / (x[1] - x[0]))

        for i in range(1, lx - 1):
            slope.append((z[i + 1] - z[i - 1]) / (x[i + 1] - x[i - 1]))
        
        slope.append((z[lx - 1] - z[lx - 2]) / (x[lx - 1] - x[lx - 2]))
        
        return np.array(slope)
    
    def findQ(self, filePath):
        """ Calculate the predicted bankfull discharge from the drainage area.
        Based on the equation Q = K*A^c where:
        Q = Discharge
        A = Drainage Area
        K,c = constants
        
        Parameters
        ------------        
        calibSet: The equation will be calibrated based on known data inputted 
                  from the calibSet argument in the form of a list of lists
                  in the format [[A,Q],...]
        self.drainageArea: This will be used to input the drainage area of the 
                           of the fluvial region in question. 
        
        Creates a plot of Drainage Area by Discharge based on the calibration 
        equation.
        """
               
        """ get calibration data """
        data = np.genfromtxt(filePath, dtype=None, delimiter=',', names=True)
        calibrationQ = data['Q']
        calibrationA = data['A']
                
        """ convert equation of form Q=kA^c to log(Q)=log(k)+c*log(A) """
        logA = [np.log10(A) for A in calibrationA]
        logQ = [np.log10(Q) for Q in calibrationQ]
        coefs = np.polynomial.polynomial.polyfit(logA, logQ, 1) 
        
        """ coeffecients are in the form of [log10(K), c] """
        K = 10**coefs[0]
        c = coefs[1]
        self.estimQ = np.array([K * (area**c) for area in self.drainageArea])
        
        plt.figure(num=3)
        plt.scatter(self.drainageArea, self.estimQ, marker='.')
        plt.xlabel('Drainage Area')
        plt.ylabel('Estimated Discharge')
        
        plt.show()
   
   def map_channel(filePath, xsections, self):
        """
        Creates a map of the channel using longitudinal profile data that 
        includes markers indicating where any and all crosssections have been
        taken.
        
        Paramenters
        -----------
        filePath:  A string of the directory to the channel domain. 
                   (this is the .channel file)
        xsections: a list of strings of the directories to the xsection 
                   domains that will be marked on the map. (these are the 
                   .xsection files)
        -----------

        Example format for input domains are located in dataFileTemplates.
        """
        xSectionList = []
        
        for path in xsections:
            with open(path,'r') as f_in:
                next(f_in)
                next(f_in)
                coordString = f_in.readline()
                coordString = coordString[:-1]
                coordList = coordString.split(',')
                coords = [float(number)for number in coordList]
                xSectionList.append(coords)
        xCoordPoints = [coord[0] for coord in xSectionList]
        yCoordPoints = [coord[1] for coord in xSectionList]
            
        plt.figure(num=4)
        plt.plot(self.x, self.y, 'k', xCoordPoints, yCoordPoints, 'ro')
        plt.xlabel('Easting')
        plt.ylable('Northing')
     
    def plot(self):
        """ Plot channel map and longitudinal profile parameters. 
        
        """
        
        plt.figure()
        plt.plot(self.x, self.y, 'k')
        plt.xlabel('easting')
        plt.ylabel('northing')
        plt.gca().set_aspect('equal', adjustable='box')
        
        plt.figure()
        
        plt.subplot(4, 1, 1)
        plt.plot(self.distanceFromMouth, self.elevation, 'k')
        plt.xlabel('distance from mouth')
        plt.ylabel('elevation')
        
        plt.subplot(4, 1, 2)
        plt.plot(self.distanceFromMouth, self.slope, 'k')
        plt.xlabel('distance from mouth')
        plt.ylabel('slope')

        plt.subplot(4, 1, 3)
        plt.plot(self.distanceFromMouth, self.drainageArea, 'k+')
        plt.xlabel('distance from mouth')
        plt.ylabel('drainage area')
        
        plt.subplot(4, 1, 4)
        plt.plot(self.distanceFromMouth, self.estimQ, 'k+')
        plt.xlabel('distance from mouth')
        plt.ylabel('discharge')
                
        plt.show()
        
    def predict_bed_grain_size(self, parameters):
        """ Predict reach-averaged streambed grain size.
        
        Estimate bed shear stress
        tb = waterDensity * gravitationalAcceleration * manningsn^(3/5) .* Q.^(3/5) .* w.^(-3/5) .* (S.^(7/10))
        
        Estimate grain size
        grainSize = tb / ((ps - waterDensity) .* gravitationalAcceleration .* tc)
        
        """        
        
        """ width estimation """
        kw = 1.06e-32
        b = 3.71
        self.width = (kw * self.drainageArea**b)        
        
        bedShearStress = self.estimQ.dot(parameters.waterDensity * parameters.gravitationalAcceleration * parameters.manningsn) * self.width**(-3/5) * self.slope**(7/10)