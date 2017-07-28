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
        

    def new_game_or_exit(self):
        inputstr = raw_input('Press Return key to start new game or type "exit" and hit Return to exit.')
        if inputstr != "exit":
            self.start_new_game()
        print('Exit game. See you next time.')
    
    
    def start_game(self):
        self.goal_input_handler.manage()
        
        for curr_round in xrange(ROUND_NUMBER):
            print('Round %s of %s') % (curr_round+1, ROUND_NUMBER)
            self.player_input_handler.manage()
            self.player_codes.manage()
            self.evaluator.manage()
            if self.evaluator.is_won():
                print("CONGRATULATIONS!")
                self.new_game_or_exit()
                break
                        
            elif self.evaluator.is_lost():
                print("You can do it! Try again.")
                self.new_game_or_exit()
                break

    def start_new_game(self):
        self.clear_gamestate()
        self.start_game()
        
    def clear_gamestate(self):
        self.evaluator.reset()
