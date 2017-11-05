'''
    Created on Apr 12, 2016
    @author: Nawrin Sultana
'''
import Assignment.prod.Latitude as LT
import unittest
from datetime import date, time

class LatitudeTest(unittest.TestCase):
    # 100 constructor
    # Happy path

    def test100_010_ShouldConstruct(self):
        degrees = 60
        minutes = 20.5
        hemisphere = 'S'
        self.assertIsInstance(LT.Latitude(degrees, minutes, hemisphere), LT.Latitude)
        
    def test100_020_ShouldConstructWithOutOptionalParam(self):
        degrees = 60
        minutes = 20.5
        self.assertIsInstance(LT.Latitude(degrees, minutes), LT.Latitude)
        
    # Sad path tests

    def test100_910_ShouldNotConstructOnMissingDegree(self):
        expectedString = "Latitude.__init__:"
        with self.assertRaises(ValueError) as context:
            LT.Latitude(minutes=20.5)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Missing Mandatory Parameter")
        
    def test100_920_ShouldNotConstructOnNonIntegerDegree(self):
        expectedString = "Latitude.__init__:"
        with self.assertRaises(ValueError) as context:
            LT.Latitude(degrees=60.5, minutes=20.5)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Parameter Type")
    
    def test100_930_ShouldNotConstructOnOutOfBoundDegreeValue(self):
        expectedString = "Latitude.__init__:"
        with self.assertRaises(ValueError) as context:
            LT.Latitude(degrees = 100, minutes=20.5)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Bound of Parameter")
        
    def test100_940_ShouldNotConstructOnMissingMinute(self):
        expectedString = "Latitude.__init__:"
        with self.assertRaises(ValueError) as context:
            LT.Latitude(degrees=60, hemisphere='S')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Missing Mandatory Parameter")
        
    def test100_950_ShouldNotConstructOnNonNumericMinute(self):
        expectedString = "Latitude.__init__:"
        with self.assertRaises(ValueError) as context:
            LT.Latitude(degrees=60.5, minutes='20.5')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Parameter Type")
    
    def test100_960_ShouldNotConstructOnOutOfBoundMinuteValue(self):
        expectedString = "Latitude.__init__:"
        with self.assertRaises(ValueError) as context:
            LT.Latitude(degrees = 60, minutes=61)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Major:  failure to check Bound of Parameter")
        
    # 200 getDegrees
    # Happy Path

    def test200_010_ShouldReturnDegrees(self):
        degrees = 60
        minutes = 20.5
        latitude = LT.Latitude(degrees, minutes)
        self.assertEquals(degrees, latitude.getDegrees())
        
    # 300 getMinutes
    # Happy Path

    def test300_010_ShouldReturnMinute(self):
        degrees = 60
        minutes = 20.5
        latitude = LT.Latitude(degrees, minutes)
        self.assertEquals(minutes, latitude.getMinutes())
        
    # 400 getHemisphere
    # Happy Path

    def test400_010_ShouldReturnDefaultHemisphere(self):
        degrees = 60
        minutes = 20.5
        latitude = LT.Latitude(degrees, minutes)
        self.assertEquals(1, latitude.getHemisphere())
        
    def test400_020_ShouldReturnPassedHemisphere(self):
        degrees = 60
        minutes = 20.5
        hemisphere = 'S'
        latitude = LT.Latitude(degrees, minutes, hemisphere)
        self.assertEquals(-1, latitude.getHemisphere())
        
    def test400_030_ShouldReturnEmptyHemisphere(self):
        degrees = 0
        minutes = 0
        latitude = LT.Latitude(degrees, minutes)
        self.assertEquals(0, latitude.getHemisphere())  
        
    # 500 getString
    # Happy Path

    def test500_010_ShouldReturnStringForLatitude(self):
        degrees = 60
        minutes = 20.5
        hemisphere = 'N'
        latitude = LT.Latitude(degrees, minutes, hemisphere)
        self.assertEquals('N60 20.5', latitude.getString()) 
        
    def test500_020_ShouldReturnString(self):
        degrees = 0
        minutes = 0
        latitude = LT.Latitude(degrees, minutes)
        self.assertEquals('0 0.0', latitude.getString())