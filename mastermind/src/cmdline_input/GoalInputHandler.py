'''
Created on 10.09.2014

@author: proSingularity
'''
from util.IManageable import IManageable
from cmdline_input.ITupleInput import ITupleInput
from util.Settings import COLORS, STONE_NUMBER

class GoalInputHandler(IManageable, ITupleInput):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.tuple = None

    def get_tuple(self):
        return self.tuple
            
    def manage(self):
        ''' ask for a new input tuple, until it fulfills the conditions defined in the Settings '''
        while True:
            incoming = raw_input("Please insert your goal combination, i.e. the one the other player must guess. Example: 'red blue yellow white blue':\n")
            try:
                incoming_list = incoming.split()
                # consistency test
                if len(incoming_list) == STONE_NUMBER:
                    combi = [COLORS[color] for color in incoming_list]
                    self.tuple = combi
                    break
            except: KeyError("Non-valid value found.")
