import os #for getting filenames & current user's folder
import json
from time import sleep


class EliteEventStreamer:
    logfolderpath = os.environ['userprofile']+r"\Saved Games\Frontier Developments\Elite Dangerous"

    def __init__(self):
        os.chdir(EliteEventStreamer.logfolderpath)
        filepaths = [x for x in os.listdir() if '.log' in x]
        filepaths.sort()
        self.currentlogfile = open(filepaths[-1])

    def getEvents(self): # get all events since last call
        return [json.loads(x) for x in self.currentlogfile.readlines()]
        
