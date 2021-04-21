import re
import glob
import os
from fileStats import *

class directoryStats:

    files = []
    linesPerMethod = 0
    linesPerClass = 0
    ratioInOut = 0
    avgNumParams = 0
    percentInClasses = 0
    percentOutClasses = 0
    percentInMethods = 0
    percentOutMethods = 0

    def __init__(self, directoryName):

        #get all python files in directory
        paths =  glob.glob(os.getcwd()+"/"+directoryName+"/*.py")
        paths += glob.glob(os.getcwd()+"/"+directoryName+"/*/*.py")

        #for each file:
        for p in paths:
            #make fileStats obj and add to list
            try:
                self.files.append(fileStats(p))
            except:
                print(f"did not work for file: {p}")

        self.processDirectory()

    def getNumLines(self):

        return sum([f.getNumLines() for f in self.files])

    def getNumCommentLines(self):

        return sum([f.getNumCommentLines() for f in self.files])

    def getNumClasses(self):

        return sum([f.getNumClasses() for f in self.files])

    def getNumMethods(self):

        return sum([f.getNumMethods() for f in self.files])

    def getTotalParams(self):

        return sum([f.getTotalParams() for f in self.files])

    def getLinesInMethods(self):

        return sum([f.getLinesInMethods() for f in self.files])

    def getLinesNotInClasses(self):

        return sum([f.getLinesNotInClasses() for f in self.files])

    def getLinesInClasses(self):

        return sum([f.getLinesInClasses() for f in self.files])

    def getNumFiles(self):

        return len(self.files)

    def getLinesPerMethod(self):

        return self.linesPerMethod

    def getLinesPerClass(self):

        return self.linesPerClass

    def getRatioInOut(self):

        return self.ratioInOut

    def getAvgNumParams(self):

        return self.avgNumParams

    def getPercentInClasses(self):

        return self.percentInClasses

    def getPercentOutClasses(self):

        return self.percentOutClasses

    def getPercentInMethods(self):

        return self.percentInMethods

    def getPercentOutMethods(self):

        return self.percentOutMethods

    def getAllParams(self):

        return [item for sublist in [f.getParams() for f in self.files] for item in sublist]

    def getDefaultParams(self):

        params = self.getAllParams()

        return [p for p in params if '=' in p]

    def getMutableParamsCount(self):

        defaults = [p.split('=')[-1] for p in self.getDefaultParams()]
        mutables = ['[]','{}','[ ]','{ }','set()','set( )']

        return len([p for p in defaults if p in mutables])

    def getNumNestedLoops(self):

        return sum([f.getNumNestedLoops() for f in self.files])

    def getNumEnumerateIssues(self):

        return sum([f.getNumEnumerateIssues() for f in self.files])

    def processDirectory(self):

        print(f"number of methods: {self.getNumMethods()}")
        print(f"number of lines: {self.getNumLines()}")
        #getLinesPerMethod
        self.linesPerMethod = self.getLinesInMethods() / self.getNumMethods()

        #getLinesPerClass
        self.linesPerClass = self.getLinesInClasses() / self.getNumClasses()

        #getRatioInOut
        self.ratioInOut = self.getLinesInClasses() / self.getLinesNotInClasses()

        #getAvgNumParams
        self.avgNumParams = self.getTotalParams() / self.getNumMethods()

        #getPercentInClasses
        self.percentInClasses = self.getLinesInClasses() / self.getNumLines() * 100

        #getPercentOutClasses
        self.percentOutClasses = 100 - self.percentInClasses

        #getPercentInMethods
        self.percentInMethods = self.getLinesInMethods() / self.getNumLines() * 100

        #getPercentOutMethods
        self.percentOutMethods = 100 - self.percentInMethods
