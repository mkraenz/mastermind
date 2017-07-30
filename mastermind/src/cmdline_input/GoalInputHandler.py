'''
Created on 10.09.2014

@author: proSingularity
'''
from util.IManageable import IManageable
from cmdline_input.ITupleInput import ITupleInput
from util.Settings import COLORS, CODELENGTH
from random import randint

class GoalInputHandler(IManageable, ITupleInput):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.tuple = None

    def get_tuple(self):
        return self.tuple
    
    def get_random_combination(self):
        # if some numbers are switched of this does not make sense
        # better use Settings.COLORS.values and randomly choose out of this collection
        return [randint(0, len(COLORS)) for _ in xrange(CODELENGTH)]
            
    def manage(self):
        ''' ask for a new input tuple, until it fulfills the conditions defined in the Settings '''
        while True:
            incoming = raw_input("Please insert your goal combination, i.e. the one the other player must guess. Example: 'red blue yellow white blue':\n")
            try:
                incoming_list = incoming.split()
                # consistency test
                if len(incoming_list) == CODELENGTH:
                    combi = [COLORS[color] for color in incoming_list]
                    self.tuple = combi
                    break
            except: KeyError("Non-valid value found.")

if __name__ == '__main__':
    g = GoalInputHandler()
    print(g.randomCombination())