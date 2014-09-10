'''
Created on 10.09.2014

@author: proSingularity
'''
from util.Settings import ROUND_NUMBER

class GameManager(object):

    def __init__(self, player_codes, player_input_handler, goal_input_handler, evaluator):
        self.player_codes = player_codes
        self.player_input_handler = player_input_handler
        self.goal_input_handler = goal_input_handler
        self.evaluator = evaluator
        
    def start_game(self):
        self.goal_input_handler.manage()
        
        for i in xrange(ROUND_NUMBER):
            self.player_input_handler.manage()
            self.player_codes.manage()
            self.evaluator.manage()
            if self.evaluator.is_won():
                print("CONGRATULATIONS!")
                break
            
            # TODO: might be unneccessary
            elif self.evaluator.is_lost():
                print("Too Bad....")
                break
