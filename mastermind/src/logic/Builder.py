'''
Created on 10.09.2014

@author: proSingularity
'''
from cmdline_input.PlayerInputHandler import PlayerInputHandler
from logic.PlayerCodes import PlayerCodes
from cmdline_input.GoalInputHandler import GoalInputHandler
from logic.Evaluator import Evaluator
from logic.GameManager import GameManager

class Builder(object):

    def create(self):
        player_input_handler = PlayerInputHandler()
        player_codes = PlayerCodes(player_input_handler)
        
        goal_input_handler = GoalInputHandler()
        evaluator = Evaluator(goal_input_handler, player_codes)
        
        game_manager = GameManager(player_codes, player_input_handler, goal_input_handler, evaluator)
        return game_manager