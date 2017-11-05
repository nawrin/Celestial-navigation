'''
    Created on Mar 15, 2016
    @author: Nawrin Sultana
'''
import Assignment.prod.Sighting as ST
import unittest
import random
from datetime import date, time, tzinfo, timedelta

ZERO = timedelta(0)
HOUR = timedelta(hours=1)


class SightingTest(unittest.TestCase):

    # 100 constructor
    # Happy path test

    def test100_010_ShouldConstruct(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        self.assertIsInstance(ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                                          temperature, pressure, artificialHorizon), ST.Sighting)

    def test100_020_ShouldConstruct(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = 58, 29.2
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals('Aldebaran', sighting.body)

    def test100_030_ShouldConstructWithoutOptionalParam(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)

        self.assertIsInstance(
            ST.Sighting(body, dateOfObservation, timeOfObservation, altitude), ST.Sighting)

# Sad path tests

    def test100_910_ShouldNotConstructOnMissingBody(self):
        expectedString = "Sighting.__init__:"
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(date=dateOfObservation, time=timeOfObservation, altitude=(58, 29.2), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Missing Mandatory Parameter")

    def test100_920_ShouldNotConstructOnLengthLessThanOneForBody(self):
        expectedString = "Sighting.__init__:"

        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(body='a', date=dateOfObservation, time=timeOfObservation, altitude=(58, 29.2), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check length of Parameter")

    def test100_930_ShouldNotConstructOnNonStringBody(self):
        expectedString = "Sighting.__init__:"

        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(body=10, date=dateOfObservation, time=timeOfObservation, altitude=(58, 29.2), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check type of Parameter")

    def test100_940_ShouldNotConstructOnNonDateObject(self):
        expectedString = "Sighting.__init__:"

        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(body='Aldebaran', date="2016-03-01", time=timeOfObservation, altitude=(58, 29.2), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check type of Parameter")

    def test100_950_ShouldNotConstructOnAltitudeWithOneElementTuple(self):
        expectedString = "Sighting.__init__:"

        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(body='Aldebaran', date="2016-03-01", time=timeOfObservation, altitude=(58,), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check proper format of Parameter")

    def test100_960_ShouldNotConstructOnAltitudeWithNonIntegerDegree(self):
        expectedString = "Sighting.__init__:"

        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(body='Aldebaran', date="2016-03-01", time=timeOfObservation, altitude=('abc', 29.2), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check type of Parameter")

    def test100_970_ShouldNotConstructOnAltitudeWithOutOfRangeMinute(self):
        expectedString = "Sighting.__init__:"

        timeOfObservation = time(23, 20, 1, tzinfo=UTC())

        with self.assertRaises(ValueError) as context:
            ST.Sighting(body='Aldebaran', date="2016-03-01", time=timeOfObservation, altitude=(58, 60), height=6.0,
                        temperature=100, pressure=1000, artificialHorizon=True)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check range of Parameter")

# 200 getBody
# Happy Path

    def test200_010_ShouldReturnBody(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = 58, 29.2
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals('Aldebaran', sighting.getBody())

# 300 getDate
# Happy Path

    def test300_010_ShouldReturnDate(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 4, 2)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = 58, 29.2
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(dateOfObservation, sighting.getDate())

# 400 getTime
# Happy Path

    def test400_010_ShouldReturnTime(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = 58, 29.2
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(timeOfObservation, sighting.getTime())

    def test500_010_ShouldReturnAltitude(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 51.49)
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(58, sighting.getAltitude()[0])
        self.assertAlmostEquals(51.4, sighting.getAltitude()[1], 1)

    def test600_010_ShouldReturnHeight(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(6.0, sighting.getHeight())

    def test600_020_ShouldReturnDefaultHeight(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body=body, date=dateOfObservation, time=timeOfObservation, altitude=altitude,
                               temperature=temperature, pressure=pressure, artificialHorizon=artificialHorizon)
        self.assertEquals(0.0, sighting.getHeight())

    def test700_010_ShouldReturnTemperature(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(100, sighting.getTemperature())

    def test800_010_ShouldReturnPressure(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(1000, sighting.getPressure())

    def test900_010_ShouldReturnArtificialHorizon(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (58, 29.2)
        height = 6.0
        temperature = 100
        pressure = 1000
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(True, sighting.isArtificialHorizon())

    def test1000_010_ShouldReturnCorrectedAltitude(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (15, 4.6)
        height = 6.0
        temperature = 72
        pressure = 1010
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(14, sighting.getAltitudeCorrection()[0])
        self.assertAlmostEquals(58.8, sighting.getAltitudeCorrection()[1], 1)

    def test1000_020_ShouldReturnCorrectedAltitude(self):
        body = 'Aldebaran'
        dateOfObservation = date(2016, 3, 1)
        timeOfObservation = time(23, 20, 1, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        self.assertEquals(35, sighting.getAltitudeCorrection()[0])
        self.assertAlmostEquals(10.6, sighting.getAltitudeCorrection()[1], 1)
    
    # 1100 getGHA    
    # Happy Path 
    
    def test1100_010_ShouldReturnGHA(self):
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True

        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        
        gha = sighting.getGHA('aries.txt', 'stars.txt')
        self.assertEquals('75*54.3', gha[0])
        self.assertEquals('7*24.3', gha[1])

    # Sad Path
    
    def test1100_910_ShouldFailForMissingAriesFile(self):
        expectedString = "Sighting.getGHA:"
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True
        
        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        
        with self.assertRaises(ValueError) as context:
            sighting.getGHA(stars='stars.txt')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check mandatory Parameter")
        
    def test1100_920_ShouldFailForMissingStarsFile(self):
        expectedString = "Sighting.getGHA:"
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True
        
        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        
        with self.assertRaises(ValueError) as context:
            sighting.getGHA(aries='aries.txt')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check mandatory Parameter")
        
    def test1100_930_ShouldFailForWrongParameterType(self):
        expectedString = "Sighting.getGHA:"
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True
        
        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        
        with self.assertRaises(ValueError) as context:
            sighting.getGHA(aries='aries.txt', stars=123)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check type of Parameter")
        
    def test1100_940_ShouldRaiseErrorOnMissingFile(self):
        expectedString = "Sighting.getGHA:"
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True
        
        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        randomFileName = ''.join(random.choice('abcd01234') for x in range(8)) + "txt"
        with self.assertRaises(ValueError) as context:
            sighting.getGHA(aries='aries.txt',stars=randomFileName)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for missing file")
        
    def test200_950_ShouldRaiseErrorOnBadFileName(self):
        expectedString = "Sighting.getGHA:"
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True
        
        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        with self.assertRaises(ValueError) as context:
            sighting.getGHA("", "stars.txt")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid file name")
        
    def test200_960_ShouldRaiseErrorOnBadFileContent(self):
        expectedString = "Sighting.getGHA:"
        body = 'Betelgeuse'
        dateOfObservation = date(2016, 1, 17)
        timeOfObservation = time(3, 15, 42, tzinfo=UTC())
        altitude = (35, 14.8)
        height = 9
        temperature = 72
        pressure = 1010
        artificialHorizon = True
        
        sighting = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                               temperature, pressure, artificialHorizon)
        with self.assertRaises(ValueError) as context:
            sighting.getGHA("ariesBad.txt", "stars.txt")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check for invalid file name")
        
class UTC(tzinfo):

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO
