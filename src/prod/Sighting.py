'''
    Created on Mar 15, 2016
    @author: Nawrin Sultana
'''
import math
from datetime import date as Date, time as Time, datetime
from numbers import Number
from __builtin__ import int


class Sighting:

    def __init__(self, body=None, date=None, time=None, altitude=None, height=0.0, temperature=72.0, pressure=1010, artificialHorizon=False):
        functionName = "Sighting.__init__:  "
        if (body == None):
            raise ValueError(functionName + "missing mandatory parameter body")

        if (not(isinstance(body, str))):
            raise ValueError(functionName + "body should be of type String")

        if (len(body) <= 1):
            raise ValueError(
                functionName + "body length should be greater than 1")

        if (date == None):
            raise ValueError(functionName + "missing mandatory parameter date")

        if (not(isinstance(date, Date))):
            raise ValueError(
                functionName + "missing proper datetime.date format")

        if (time == None):
            raise ValueError(functionName + "missing mandatory parameter time")

        if (not(isinstance(time, Time))):
            raise ValueError(
                functionName + "missing proper datetime.time format")

        if (altitude == None):
            raise ValueError(
                functionName + "missing mandatory parameter altitude")
        
        if (isinstance(altitude, Number)):
            raise ValueError(functionName + "altitude must be a tuple")
        
        if (len(altitude) != 2):
            raise ValueError(
                functionName + "altitude should be a tuple of two elements")

        if (not(isinstance(altitude[0], int))):
            raise ValueError(
                functionName + "degree of altitude should be integer")

        if ((altitude[0] < 0) or (altitude[0] >= 90)):
            raise ValueError(functionName + "degree of altitude out of range")

        if (not(isinstance(altitude[1], Number))):
            raise ValueError(
                functionName + "minute of altitude should be Number")

        if ((altitude[1] < 0) or (altitude[1] >= 60)):
            raise ValueError(functionName + "minute of altitude out of range")

        if (not(isinstance(height, Number))):
            raise ValueError(functionName + "height should be Numeric")

        if (height < 0):
            raise ValueError(functionName + "height should be greater than 0")

        if (not(isinstance(temperature, Number))):
            raise ValueError(
                functionName + "temperature should be of numeric type")

        if ((temperature < -20) or (temperature > 120)):
            raise ValueError(functionName + "temperature out of range")

        if (not(isinstance(pressure, Number))):
            raise ValueError(
                functionName + "pressure should be of numeric type")

        if ((pressure < 100) or (pressure > 1100)):
            raise ValueError(functionName + "pressure out of range")

        self.body = body
        self.date = date
        self.time = time
        self.altitude = altitude
        self.height = height
        self.temperature = temperature
        self.pressure = pressure
        self.artificialHorizon = artificialHorizon

    def getBody(self):
        return self.body

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getAltitude(self):
        arcMinute = round(self.altitude[1] * 5) / 5
        return (int(self.altitude[0]), arcMinute)

    def getHeight(self):
        return self.height

    def getTemperature(self):
        return self.temperature

    def getPressure(self):
        return self.pressure

    def isArtificialHorizon(self):
        return self.artificialHorizon

    def getAltitudeCorrection(self):
        if (self.getAltitude()[0] == 0 and self.getAltitude()[1] < 0.2):
            raise ValueError(
                "Sighting.getAltitudeCorrection:  observed altitude too small")

        if (self.isArtificialHorizon()):
            dip = (-0.97 * math.sqrt(self.getHeight())) / 60
        else:
            dip = 0

        refractionPartOne = (-0.00452 * self.getPressure())
        celsiusTemperature = (self.getTemperature() - 32) * 5 / float(9)
        refractionPartTwo = 273 + celsiusTemperature
        angle = self.getAltitude()[0] + (self.getAltitude()[1] / float(60))
        refractionPartThree = math.tan(angle * (math.pi / 180))

        refraction = refractionPartOne / \
            refractionPartTwo / refractionPartThree

        correctedAltitude = angle + dip + refraction
        correctedDegree = self.getIntegerDegree(correctedAltitude)
        correctedMinute = (correctedAltitude - correctedDegree) * 60
        correctedMinute = round(correctedMinute * 5) / 5

        return (correctedDegree, correctedMinute)
    
    def getGHA(self, aries=None, stars=None):
        functionName = "Sighting.getGHA:  "
        if (aries == None or stars == None):
            raise ValueError(functionName + "file name missing")
        
        if ((not(isinstance(aries, str))) or (not(isinstance(stars, str)))):
            raise ValueError(functionName + "file type must be string")
        try:
            with open(stars, 'r') as starFile:
                initialList = []
                for line in starFile:
                    try:
                        initialList = line.split('\t')
                        if (initialList[0] == self.getBody()):
                            dateOfObservation = datetime.strptime(initialList[1], '%m/%d/%y').date()
                            if (dateOfObservation <= self.getDate()):
                                latitude = initialList[3].rstrip('\n')
                                shaStar = initialList[2]
                    except ValueError:
                        raise ValueError(functionName + "can not parse file")
                    
                starFile.close()
            try:
                with open(aries, 'r') as ariesFile:
                    for line in ariesFile:
                        try:
                            initList = line.split('\t')
                            observationDate = datetime.strptime(initList[0], '%m/%d/%y').date()
                            observationHour = self.getTime().hour
                            observationHour1 = observationHour + 1
                            ariesHour = int(initList[1])
                            if (observationDate == self.getDate() and observationHour == ariesHour):
                                GHAAries1 = initList[2]
                            if (observationDate == self.getDate() and observationHour1 == ariesHour):
                                GHAAries2 = initList[2]
                        except ValueError:
                            raise ValueError(functionName + "can not parse file")
                        
                    s = self.getTime().minute * 60 + self.getTime().second
                    aries1 = GHAAries1.split('*')
                    aries2 = GHAAries2.split('*')
                    aries1Degree = self.getIntegerDegree(aries1[0]) + self.getDegreFromMinute(float(aries1[1]))
                    aries2Degree = self.getIntegerDegree(aries2[0]) + self.getDegreFromMinute(float(aries2[1]))
                    GHAAries = aries1Degree + (abs(aries2Degree - aries1Degree) * (s / float(3600)))
                    
                    GHAAriesDegree = self.getIntegerDegree(GHAAries)
                    GHAAriesMinute = (GHAAries - GHAAriesDegree) * 60
                    GHAAriesMinute = round(GHAAriesMinute * 10) / 10
                    
                    GHAAries = str(GHAAriesDegree)+'*'+str(GHAAriesMinute)
                    
                    sha = shaStar.split('*')
                    shaStarDegree = self.getIntegerDegree(sha[0]) + self.getDegreFromMinute(float(sha[1]))
                    ariesDegree = GHAAriesDegree + self.getDegreFromMinute(GHAAriesMinute)
                    GHAObservation = ariesDegree + shaStarDegree
                    
                    GHAObservation = GHAObservation % 360
                    
                    GHAObservationDegree = self.getIntegerDegree(GHAObservation)
                    GHAObservationMinute = (GHAObservation - GHAObservationDegree) * 60  
                    GHAObservationMinute = round(GHAObservationMinute * 10) / 10
                    
                    GHA = str(GHAObservationDegree) + '*' + str(GHAObservationMinute)
                    ariesFile.close()
            except IOError:
                raise ValueError(functionName + "file not found")        
        except IOError:
            raise ValueError(functionName + "file not found")
        
        return (GHA, latitude)
    
    def getIntegerDegree(self, degree):
        return int(degree)
    
    def getDegreFromMinute(self, minute):
        return minute / float(60)