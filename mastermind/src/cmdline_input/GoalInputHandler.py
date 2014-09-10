'''
Created on 10.09.2014

@author: proSingularity
'''
from util.IManageable import IManageable
from cmdline_input.ITupleInput import ITupleInput
from model.Settings import COLORS, STONE_NUMBER

class GoalInputHandler(IManageable, ITupleInput):
    '''
    classdocs
    '''

    tuple = None
    


    def get_tuple(self):
        return self.tuple
            
    def manage(self):
        ''' ask for a new input tuple, until it fulfills the conditions defined in the Settings '''
        while True:
            incoming = raw_input("Please insert your combination, e.g. 'red blue yellow pink blue':\n")
            try:
                incoming_list = incoming.split()
                # consistency test
                if len(incoming_list) == STONE_NUMBER:
                    combi = [COLORS[color] for color in incoming_list]
                    self.tuple = combi
                    break
            except: KeyError("Non-valid value found.")
            finally:
                pass
        return