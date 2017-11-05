'''
    Created on Feb 19, 2016
    @author: Nawrin Sultana
'''
from numbers import Number

class StarCatalog:

    def __init__(self):
        self.stars = {}
        

    def loadCatalog(self, starFile=None, magnitude=6.0):
        if (self.stars):
            loadedStars = self.stars.copy()
        else:
            loadedStars = {}   
        if (starFile == None):
            raise ValueError(
                'StarCatalog.loadCatalog:  Mandatory parameter starFile is missing')

        if (not(isinstance(starFile, str))):
            raise ValueError(
                'StarCatalog.loadCatalog:  File name should be string type')

        if (len(starFile) < 1):
            raise ValueError(
                'StarCatalog.loadCatalog:  File name length should be greater or equal 1')

        if (not(isinstance(magnitude, Number))):
            raise ValueError(
                'StarCatalog.loadCatalog:  Value of magnitude should be numeric')

        if ((magnitude <= -30) or (magnitude >= 30)):
            raise ValueError(
                'StarCatalog.loadCatalog:  Magnitude is out of bound')
        try:
            with open(starFile, 'r') as f:
                
                count = 0
                for line in f:
                       
                    starId = line[0:6].strip(' ')
                    if ((starId == None) or (not(isinstance(starId, str)))):
                        raise ValueError('StarCatalog.loadCatalog:  Error during parsing starId')
                    try:
                        starMagnitude = float(line[80:84])
                    except ValueError:
                        raise ValueError('StarCatalog.loadCatalog: Bad file content for magnitude')
                        
                    if ((starMagnitude == None) or (not(isinstance(starMagnitude, Number)))):
                        raise ValueError('StarCatalog.loadCatalog:  Error during parsing magnitude')
                    try:
                        rightAscension = float(line[183:193])
                    except ValueError:
                        raise ValueError('StarCatalog.loadCatalog: Bad file content for right ascension')
                    
                    if ((rightAscension == None) or (not(isinstance(rightAscension, Number)))):
                        raise ValueError('StarCatalog.loadCatalog:  Error during parsing right ascension')
                    
                    else:
                        rightAscension = rightAscension * 57.2958
                    try:    
                        declination = float(line[194:204])
                    except ValueError:
                        raise ValueError('StarCatalog.loadCatalog: Bad file content for declination')
                    
                    if ((declination == None) or (not(isinstance(declination, Number)))):
                        raise ValueError('StarCatalog.loadCatalog:  Error during parsing declination')
                    
                    else:
                        declination = declination * 57.2958
                        
                    if (starId in self.stars):
                        self.stars.clear()
                        self.stars = loadedStars.copy()
                        raise ValueError('StarCatalog.loadCatalog:  Attempt to add duplicate star')
                            
                    if (starMagnitude <= magnitude):
                        star = []  # List to hold star information
                        star.append(starId)
                        star.append(starMagnitude)
                        star.append(rightAscension)
                        star.append(declination)
                                    
                        self.stars[starId] = star
                        count += 1
                f.close() 
        except IOError:
            raise ValueError('StarCatalog.loadCatalog:  File not found')      
        
        return count

    def emptyCatalog(self):
        numberOfStarInCatalog = len(self.stars)
        self.stars.clear()
        return numberOfStarInCatalog

    def getStarCount(self, dimmest=None, brightest=None):
        if ((dimmest != None) and not(isinstance(dimmest, Number))):
            raise ValueError(
                'StarCatalog.getStarCount:  Parameter dimmest should be numeric')

        if ((brightest != None) and not(isinstance(brightest, Number))):
            raise ValueError(
                'StarCatalog.getStarCount:  Parameter brightest should be numeric')

        if (dimmest == None):
            minReference = -31
            values = self.stars.viewvalues()
            for val in values:
                if (val[1] > minReference):
                    minReference = val[1]
            dimmest = minReference

        if (brightest == None):
            maxReference = 31
            values = self.stars.viewvalues()
            for val in values:
                if (val[1] < maxReference):
                    maxReference = val[1]
            brightest = maxReference

        count = 0
        values = self.stars.viewvalues()
        for val in values:
            if ((val[1] >= brightest) and (val[1] <= dimmest)):
                count += 1

        return count

    def getStarData(self, starId=None):
        if (starId == None):
            raise ValueError(
                'StarCatalog.getStarData:  Parameter starId is mandatory')

        if (not(isinstance(starId, str))):
            raise ValueError(
                'StarCatalog.getStarData:  Parameter starId should be string type')

        if (starId.strip() not in self.stars):
            raise ValueError(
                'StarCatalog.getStarData:  Specified star not found in catalog')

        return self.stars[starId.strip()]