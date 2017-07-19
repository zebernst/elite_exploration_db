import os #for getting filenames & current user's folder
import json
from time import sleep


class EliteEventStreamer:
    logfolderpath = os.environ['userprofile']+r"\Saved Games\Frontier Developments\Elite Dangerous"

    def __init__(self):
        os.chdir(EliteEventStreamer.logfolderpath)
        filepaths = [x for x in os.listdir() if '.log' in x]
        filepaths.sort()
        self.currentlogfilepath = filepaths[-1]
        self.currentlogfile = open(self.currentlogfilepath)
        

    def getEvents(self): # get all events since last call
        return [json.loads(x) for x in self.currentlogfile.readlines()]

    def __del__(self): #runs when reference counter <=0
        self.currentlogfile.close()

    def updateLogFile(self): # start reading from the newest log file
        filepaths = [x for x in os.listdir() if '.log' in x]
        filepaths.sort()
        self.currentlogfile.close()
        self.currentlogfilepath = filepaths[-1]
        self.currentlogfile = open(self.currentlogfilepath)

    def __repr__(self): 
        return "<{}():{}>".format(self.__class__.__name__+,self.currentlogfilepath)
        #since it is not possible to reproduce an event streamer by passing an argument
