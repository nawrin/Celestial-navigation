'''
    Created on Mar 16, 2016
    @author: Nawrin Sultana
'''
import Assignment.prod.Fix as fx
import Assignment.prod.Sighting as ST
import unittest

from datetime import date, time, tzinfo, timedelta

ZERO = timedelta(0)


class FixTest(unittest.TestCase):

    # 100 constructor
    # Happy path

    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(fx.Fix(), fx.Fix)

# 200 getSightings
# Happy Path

    def test200_010_ShouldReturnList(self):
        fix = fx.Fix()

        body = 'Aldebaran'
        dateOfObservation = date(2016, 03, 01)
        timeOfObservation = time(23, 40, 01, tzinfo=UTC())
        altitude = (15, 04.6)
        height = 6.0
        temperature = 72
        pressure = 1010
        artificialHorizon = True

        sighting1 = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                                temperature, pressure, artificialHorizon)

        body = 'Alcor'
        dateOfObservation = date(2015, 03, 01)
        timeOfObservation = time(23, 40, 01, tzinfo=UTC())
        altitude = (15, 04.6)
        height = 6.0
        temperature = 80
        pressure = 1000
        artificialHorizon = True

        sighting2 = ST.Sighting(body, dateOfObservation, timeOfObservation, altitude, height,
                                temperature, pressure, artificialHorizon)

        listOfSighting = fix.getSightings("sighting.xml")

        self.assertEquals(2, len(listOfSighting))
        self.assertEquals(sighting2.getBody(), listOfSighting[0].getBody())
        self.assertEquals(sighting1.getBody(), listOfSighting[1].getBody())

    def test200_010_ShouldReturnZeroInstanceOfSighting(self):
        fix = fx.Fix()

        listOfSighting = fix.getSightings("CA02Fix020.xml")

        self.assertEquals(0, len(listOfSighting))

    def test200_010_ShouldReturnOneInstanceOfSighting(self):
        fix = fx.Fix()

        listOfSighting = fix.getSightings("CA02Fix010.xml")

        self.assertEquals(1, len(listOfSighting))
# Sad path

    def test200_910_ShouldFailOnMissingFileName(self):
        expectedString = "Fix.getSightings:  "
        fix = fx.Fix()
        with self.assertRaises(ValueError) as context:
            fix.getSightings()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Missing Mandatory Parameter")

    def test200_920_ShouldFailOnNonStringFilename(self):
        expectedString = "Fix.getSightings:  "
        fix = fx.Fix()
        with self.assertRaises(ValueError) as context:
            fix.getSightings(123)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check type of Parameter")

    def test200_930_ShouldFailOnWrongFormatFilename(self):
        expectedString = "Fix.getSightings:  "
        fix = fx.Fix()
        with self.assertRaises(ValueError) as context:
            fix.getSightings('f01.txt')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check type of Parameter")

    def test200_940_ShouldFailOnFilenameWithLengthLessThanOne(self):
        expectedString = "Fix.getSightings:  "
        fix = fx.Fix()
        with self.assertRaises(ValueError) as context:
            fix.getSightings('.xml')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to length of Parameter")


class UTC(tzinfo):

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO
