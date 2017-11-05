'''
    Created on Apr 12, 2016
    @author: Nawrin Sultana
'''
from numbers import Number

class Latitude:
    def __init__(self, degrees=None, minutes=None, hemisphere='N'):
        functionName = "Latitude.__init__:  "
        if (degrees == None):
            raise ValueError(functionName + "missing mandatory parameter degrees")
        
        if (not(isinstance(degrees, int))):
            raise ValueError(functionName + "degrees should be of type integer")
        
        if ((degrees < 0) or (degrees > 90)):
            raise ValueError(functionName + "degrees out of bound")
        
        if (minutes == None):
            raise ValueError(functionName + "missing mandatory parameter minutes")
        
        if (not(isinstance(minutes, Number))):
            raise ValueError(functionName + "minutes should be of numeric type")
        
        if ((minutes < 0) or (minutes >= 60)):
            raise ValueError(functionName + "minutes out of range")
        
        if ((degrees == 0) and (minutes == 0)):
            hemisphere = ''
            
        self.degrees = degrees
        self.minutes = minutes
        self.hemisphere = hemisphere
        
    def getDegrees(self):
        return self.degrees
    
    def getMinutes(self):
        return round(self.minutes * 10) / float(10)    
        
    def getHemisphere(self):
        if (self.hemisphere == 'N'):
            return 1
        elif (self.hemisphere == 'S'):
            return -1
        else:
            return 0
        
    def getString(self):
        result = self.hemisphere + str(self.getDegrees()) + ' ' + str(self.getMinutes());
        return result
        
        
        