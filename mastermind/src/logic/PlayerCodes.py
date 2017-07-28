'''
Created on 10.09.2014

@author: proSingularity
'''
from logic.IPlayerCode import IPlayerCode
from util.IManageable import IManageable

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
        self.codelist.append(self.tuple_input.get_tuple())