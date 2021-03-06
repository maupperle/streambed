#! /usr/bin/env python

import glob
import os
import streambed as sb

class Model(object):
    
    """ Data structure and methods for instances of a streambed model.
    """
    
    domain = {}
    
    def __init__(self, dataDirectory):
        print('\n****************************\n')
        print('Streambed ' + sb.__version__)     
        print('\n----------------------------')
        
        self.dataDirectory = dataDirectory
        self.__set_domains()
        self.parameters = sb.Parameters()
    
    def __set_domains(self):
        channelPaths = glob.glob(self.dataDirectory + '/*.channel')
        calibrationPaths = glob.glob(self.dataDirectory + '/*.calibration')
        xsectionPaths = glob.glob(self.dataDirectory + '/*.xsection')    
        
        print('Domains in data directory:\n')
        
        self.__set_domain_type('channels', channelPaths)

        self.__set_domain_type('xsections', xsectionPaths)

        self.__set_domain_type('calibrations', calibrationPaths)           
        
        print('\n----------------------------')
    
    def __set_domain_type(self, domainTypeTitle, paths):
        print '  %s (%i):' % (domainTypeTitle, len(paths))
        
        for path in paths:
            domainTitle = os.path.splitext(os.path.basename(path))[0]
            
            print('  - ' + domainTitle)
            
            self.domain[domainTitle] = path
        
        print('\n')
        