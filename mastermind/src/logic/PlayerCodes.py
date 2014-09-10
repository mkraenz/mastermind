'''
Created on 10.09.2014

@author: proSingularity
'''
from logic.IPlayerCode import IPlayerCode
from util.IManageable import IManageable
from abc import abstractmethod

class PlayerCodes(IPlayerCode, IManageable):

    def __init__(self, tuple_input):
        '''
        Constructor
        '''
        self.codelist = []
        self.tuple_input = tuple_input
        
    def get_code(self):
        return self.codelist[-1]
    
    def manage(self):
        tuple = self.tuple_input.get_tuple()
        self.codelist.append(tuple)