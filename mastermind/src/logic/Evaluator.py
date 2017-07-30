'''
Created on 10.09.2014

@author: proSingularity
'''
from logic.IWinManager import IWinManager
from util.IManageable import IManageable
from util.Settings import CODELENGTH, ROUND_NUMBER


class Evaluator(IWinManager, IManageable):
    '''
    classdocs
    '''
    
    def __init__(self, tuple_input, player_codes):
        '''
        Constructor
        '''
        self.tuple_input = tuple_input
        self.player_codes = player_codes
        self.goal_code = None
        # eval_list contains tuples (w,s) with w pointers for correct, and s pointers for right color 
        # but wrong place
        self.eval_list = []
        
    def reset(self):
        self.goal_code = None
        self.eval_list = []
        
    def is_won(self):
        if self.eval_list[-1][0] == CODELENGTH:
            return True
        return False
    
    def is_lost(self):
        if len(self.eval_list) == ROUND_NUMBER:
            return True
        return False
    
    def manage(self):
        if self.goal_code == None:
            self.goal_code = self.tuple_input.get_tuple()
        code = self.player_codes.get_code()
        (w, s) = self.evaluate(code)
        self.eval_list.append((w, s))
        print('%s correct stones. %s in wrong position.') % (w, s)
        
    def evaluate(self, code):
        goal_code_deletable = self.goal_code[:]
        right_pos_and_color = 0
        right_color = 0
        
        for i in xrange(len(self.goal_code)):
            if code[i] == self.goal_code[i]:
                right_pos_and_color += 1
            
            for j in xrange(len(goal_code_deletable)):
                if code[i] == goal_code_deletable[j]:
                    right_color += 1
                    del goal_code_deletable[j]
                    break
                
                
        return (right_pos_and_color, right_color - right_pos_and_color)
        
        
