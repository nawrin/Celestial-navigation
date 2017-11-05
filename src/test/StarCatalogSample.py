'''
    Created on Feb 19, 2016
    @author: Nawrin Sultana
'''
import unittest
import Assignment.prod.StarCatalog as StarCatalog

class TestStarCatalog(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
# construct
    def test_100_shouldConstructStarCatalog(self):
        self.assertIsInstance(StarCatalog.StarCatalog(), StarCatalog.StarCatalog)
        
#stars = StarCatalog.StarCatalog()


# -------------- loadCatalog -----------------------------
# Load the catalog with a valid file
# The return value will be a count of the number of stars loaded
#starCount = stars.loadCatalog(starFile="Sao.Txt")
    
    def test_200_000_loadStarsFromValidFile(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        print starCount
       


# Attempts to load the catalog using a non-existent file or 
# a file that does not contain legitimate star information
# should result in a ValueError exception bearing a
# diagnostic message.
#try:
#    stars.loadCatalog(starFile="aValidStarFile.txt")
#except ValueError as e:
#    diagnosticString1 = e.args[0]

    def test_200_900_loadStarsFromInValidFile(self):
        stars = StarCatalog.StarCatalog()
        self.assertRaises(stars.loadCatalog(starFile="/home/softwareprocess/Desktop/test.txt"), ValueError)
        
# -------------- getStarCount -----------------------------
# Get a count of stars with magnitudes between 2 and 5, inclusive.
#starsBetween2And5 = stars.getStarCount(dimmest=5, brightest=2)

    def test_300_000_getStarCountBetween2and5(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        starsBetween2And5 = stars.getStarCount(dimmest=5, brightest=2)
        print starsBetween2And5
# Get a count of stars with magnitudes .LE. 5.
#starsLE5 = stars.getStarCount(brightest=5)
    def test_300_001_getStarCountWithMagnitudeLessThan5(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        starsLE5 = stars.getStarCount(brightest=5)
        print starsLE5
# Get a count of stars with magnitudes .GE. 3
#starsGE3 = stars.getStarCount(dimmest=3)
    def test_300_002_getStarCountWithMagnitudeGreaterThan3(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        starsGE3 = stars.getStarCount(dimmest=3)
        print starsGE3
# Get a count of all stars
#allStars = stars.getStarCount()
    def test_300_003_getStarCountWithAllStars(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        allStars = stars.getStarCount()
        print allStars
# Attempt to get a count of stars using an invalid magnitude
#try:
#    stars.getStarCount('a', 5)
#except ValueError as e:
#    diagnosticString2 = e.args[0]
    def test_300_900_getStarCountWithInValidMagnitude(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        self.assertRaises(stars.getStarCount('a', 5), ValueError)

# -------------- getStarData -----------------------------
# Get information associated with a specific star
#star = stars.getStarData("150340")
#  star[0] is "150340"
#  star[1] is "4.3"
#  star[2] is 79.8937753
#  star[3] is -13.176769
    def test_400_000_getStarDataWithValidStarId(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        star = stars.getStarData("1")
        self.assertEqual(star[0], "1", "Star with starId 1 not found")

# Attempt to get information on a star not present in the catalog
#try:
#    stars.getStarData("231888")
#except ValueError as e:
#    diagnosticString2 = e.args[0]
    def test_400_900_getStarDataWithInValidStarId(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        self.assertRaises(stars.getStarData("258998"), ValueError)
        

# -------------- emptyCatalog -----------------------------
# empty the catalog
#starsDeleted = stars.emptyCatalog()
    def test_500_000_emptyCatalogPass(self):
        stars = StarCatalog.StarCatalog()
        starCount = stars.loadCatalog(starFile="/home/softwareprocess/Desktop/sao.txt")
        starsDeleted = stars.emptyCatalog()
        self.assertEqual(starCount, starsDeleted, "Star catalog failed empty")