'''
    Created on Mar 16, 2016
    @author: Nawrin Sultana
'''
import Sighting
import re
from __builtin__ import str
from __builtin__ import int
from xml.dom.minidom import parse
from datetime import date, time, timedelta, tzinfo, datetime
from numbers import Number
from operator import itemgetter
from xml.dom.expatbuilder import TEXT_NODE

ZERO = timedelta(0)


class Fix:

    def __init__(self):
        self.sightingList = []

    def getSightings(self, sightingFile=None):
        functionName = "Fix.getSightings:  "
        if (self.sightingList):
            loadedList = self.sightingList.copy()
        else:
            loadedList = []

        if (sightingFile == None):
            self.setSightingList(loadedList)
            raise ValueError(
                functionName + "missing mandatory parameter file name")

        if (not(isinstance(sightingFile, str))):
            self.setSightingList(loadedList)
            raise ValueError(functionName + "file name should be string type")

        regEx = re.compile('^[\w,\s-]+\.xml')
        if (not(regEx.match(sightingFile))):
            self.setSightingList(loadedList)
            raise ValueError(functionName + "file name not in proper format")

        filePart = sightingFile.split()
        if (len(filePart[0]) < 1):
            self.setSightingList(loadedList)
            raise ValueError(functionName + "file name length less than 1")

        try:
            with open(sightingFile, 'r') as f:
                dom = parse(f)
                sightingList = self.getSightingListFromDom(
                    dom, loadedList, functionName)

        except IOError:
            self.setSightingList(loadedList)
            raise ValueError(functionName + "file not found")

        return sightingList

    def getSightingListFromDom(self, dom, loadedList, functionName):
        sightings = dom.getElementsByTagName("sighting")
        sightingList = []
        for sighting in sightings:
            name = self.getText(sighting.getElementsByTagName("body"))
            Date = self.getText(sighting.getElementsByTagName("date"))
            Time = self.getText(sighting.getElementsByTagName("time"))
            observation = self.getText(
                sighting.getElementsByTagName("observation"))
            height = self.getText(sighting.getElementsByTagName("height"))
            temperature = self.getText(
                sighting.getElementsByTagName("temperature"))
            pressure = self.getText(sighting.getElementsByTagName("pressure"))
            horizon = self.getText(sighting.getElementsByTagName("horizon"))
            
            if (name == None or Date == None or Time == None or observation == None or 
                    height == None or temperature == None or pressure == None or horizon == None):
                raise ValueError(functionName + "bad file content")
            try:
                if (str(horizon).upper() == 'Artificial'.upper()):
                    isArtificial = True
                else:
                    isArtificial = False

                dateOfObservation = datetime.strptime(Date, '%Y-%m-%d').date()

                timeOfObservation = datetime.strptime(Time, '%H:%M:%S').time()
                #partsOfTime = Time.split(':')
                #timeOfObservation = time(partsOfTime[0], partsOfTime[1], partsOfTime[2], tzinfo=UTC())
                partsOfObservation = observation.split(' ')

                altitude = (
                    int(partsOfObservation[0]), float(partsOfObservation[1]))

                sightingObject = Sighting.Sighting(str(name), dateOfObservation, timeOfObservation, altitude, float(height),
                                                   float(temperature), float(pressure), isArtificial)

            except ValueError:
                self.setSightingList(loadedList)
                raise ValueError(functionName + 'invalid content in xml file')
            sightingList.append(sightingObject)

        if (len(sightingList) > 1):
            sightingList = sorted(
                sightingList, key=lambda Sighting: (Sighting.date, Sighting.time))

        return sightingList

    def getText(self, nodeList):
        for node in nodeList:
            return node.firstChild.nodeValue

    def setSightingList(self, loadedList):
        del self.sightingList[:]
        self.sightingList = loadedList[:]


class UTC(tzinfo):

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

