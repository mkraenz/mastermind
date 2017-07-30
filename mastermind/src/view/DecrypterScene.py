'''
Created on 29.07.2017

@author: Mirco
'''
from util import Settings
from view.CrypterScene import CrypterScene
from view.Stone import Stone
from view.ViewSettings import COLORS_TO_RGB, BLOCK_SIZE
import pygame
from view import ViewSettings

class DecrypterScene(CrypterScene):
    
    def __init__(self, color_choices_stones, code_given_in_colors):
        CrypterScene.__init__(self, color_choices_stones, code_given_in_colors)
        
        self.combinations_matrix = []
        
        if Settings.DEBUG_LEVEL >= 1:
            print('Enter DecrypterScene')
            print('code_given_in_colors given to DecrypterScene =', code_given_in_colors)

    def render(self, surface):
        CrypterScene.render(self, surface)
        self._draw_combinations_matrix(surface)
            

    def handle_events(self, events):
        CrypterScene.handle_events(self, events)
        
        for event in events:
            if event.type == pygame.KEYUP and pygame.K_RETURN and \
                        self._is_valid_combination(self.current_combination_stones):
                self.check_is_won(self.current_combination_stones, self.code_given_in_colors)
                current_round = self.combinations_matrix.index(self.current_combination_stones) + 1
                if Settings.DEBUG_LEVEL >= 1:
                    print('current round = %s') %current_round
                if  current_round != Settings.ROUND_NUMBER:
                    # TODO: do logic stuff like evaluation etc
                    self.current_combination_stones = self.combinations_matrix[current_round]
                    self.selected_combination_stone = self.current_combination_stones[0]
                    pass 
                else: # we are in the final round. 
                    pass #TODO: end game
    

    
    def _handle_clicked_color_stone(self, code_given_in_colors, clicked_stone):
        if Settings.DEBUG_LEVEL >= 1:
            print 'clicked colored stone: ' + str((clicked_stone, ViewSettings.RGB_TO_COLORS[clicked_stone.color]))
            
        self.selected_combination_stone.set_color(clicked_stone.color)

    def _is_valid_combination(self, combination):
        black_stones = [stone for stone in combination if stone.color == COLORS_TO_RGB['black']]
        return True if not black_stones else False
    
    def _draw_combinations_matrix(self, surface):
        if not self.combinations_matrix:
            self._init_combinations_matrix(Settings.ROUND_NUMBER, Settings.CODELENGTH, surface)
        for row in self.combinations_matrix:
            for stone in row:
                stone.render(surface)
        
    
    def _init_combinations_matrix(self, round_number, codelength, surface):
        self.combinations_matrix = []
        for j in xrange(Settings.ROUND_NUMBER):
            combination_row = [Stone(COLORS_TO_RGB['black'], BLOCK_SIZE, BLOCK_SIZE,
                surface.get_width() / (Settings.CODELENGTH + 1) * (i + 1) - BLOCK_SIZE / 2,
                (surface.get_height()*0.8) / Settings.ROUND_NUMBER * j +10) 
                                            for i in xrange(Settings.CODELENGTH)]
            self.combinations_matrix.append(combination_row)
                                            
        self.current_combination_stones = self.combinations_matrix[0]
        self.selected_combination_stone = self.current_combination_stones[0]
        
      
    def evaluate(self, code, goal_code):
        goal_code_deletable = goal_code[:]
        right_pos_and_color = 0
        right_color = 0
        
        for i in xrange(len(goal_code)):
            if code[i] == goal_code[i]:
                right_pos_and_color += 1
            
            for j in xrange(len(goal_code_deletable)):
                if code[i] == goal_code_deletable[j]:
                    right_color += 1
                    del goal_code_deletable[j]
                    break
                
        return (right_pos_and_color, right_color - right_pos_and_color)

    def check_is_won(self, code, code_given_in_colors):
        # TODO:
        goal_code = [color for color in code_given_in_colors]
        code = [ViewSettings.RGB_TO_COLORS[stone.color] for stone in code]
        print('code = %s') %code
        print('goal_code = %s') % goal_code
        print(self.evaluate(code, goal_code))
        return self.evaluate(code, goal_code)