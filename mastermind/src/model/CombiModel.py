'''
Created on 04.09.2014

@author: proSingularity
'''

from cmdline_input.CombiReader import CombiReader
from itertools import combinations
from model import Settings
import random

class CombiModel(object):
    '''
    classdocs
    '''

    target = []
    combinations = []
    combireader = None

    def __init__(self):
        '''
        Constructor
        '''
        self.combireader = CombiReader()

    def setTarget(self, new_target):
        self.target = new_target
        
    def setCombi(self, combi):
        combinations.attach(combi)
        
    def getTarget(self):
        return self.target
    
    def getCombis(self):
        return self.combinations
    
    def readFromCmd(self):
        prev_length = len(self.getCombis())
        while prev_length == len(self.getCombis()):
            combi = self.combireader.read_cmd()
            if combi != None:
                self.setCombi(combi)
    
    def createTargetUniform(self):
        new_target = [random.randint(0, len(Settings.COLORS)-1) for i in xrange(Settings.STONE_NUMBER)]
        self.setTarget(new_target)
        return self.getTarget()
            