'''
Created on 10.09.2014

@author: proSingularity
'''
from logic.Builder import Builder

if __name__ == '__main__':
    game_manager = Builder().create()
    game_manager.start_game()