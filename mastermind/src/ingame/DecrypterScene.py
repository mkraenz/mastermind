'''
Created on 29.07.2017

@author: Mirco
'''
from settings import Settings
import pygame
from metagame.WinScene import WinScene
from metagame.GameOverScene import GameOverScene
from settings.ViewSettings import RGB_TO_COLORS, COLORS_TO_RGB, BLOCK_SIZE
from ingame.Stone import Stone
from ingame.CrypterScene import CrypterScene

class DecrypterScene(CrypterScene):
    
    def __init__(self, color_choices_stones, code_given_in_colors):
        CrypterScene.__init__(self, color_choices_stones, code_given_in_colors)
        
        self.combinations_matrix = []
        self.results_tuples = []  # contains result_tuples (correct stones, correct color)
                                    # parallel to combination matrix
        
        if Settings.DEBUG_LEVEL >= 1:
            print('Enter DecrypterScene')

    def render(self, surface):
        CrypterScene.render(self, surface)
        self._draw_combinations_matrix(surface)
        self._draw_result_tuples(surface)
            

    def handle_events(self, events):
        CrypterScene.handle_events(self, events)
        
        for event in events:
            if event.type == pygame.KEYUP and pygame.K_RETURN and \
                        self._is_valid_combination(self.current_combination_stones):
                current_round = self.combinations_matrix.index(self.current_combination_stones) + 1
                self.results_tuples.append(self.get_result_tuple()) 
                if Settings.DEBUG_LEVEL >= 1:
                    print('current round = %s') % current_round
                    print(self.results_tuples[current_round - 1])
                
                if self.check_is_won(self.results_tuples[current_round - 1]):
                    self.manager.go_to(WinScene())
                elif self.check_is_lost(current_round):
                    self.manager.go_to(GameOverScene())
                else:  # game continues
                    self.current_combination_stones = self.combinations_matrix[current_round]
                    self.selected_combination_stone = self.current_combination_stones[0]
            if Settings.DEBUG_LEVEL >= 2:
                if event.type == pygame.KEYUP and event.key == pygame.K_w:
                    self.manager.go_to(WinScene())
                if event.type == pygame.KEYUP and event.key == pygame.K_l:
                    self.manager.go_to(GameOverScene())
    
    def get_result_tuple(self):
        goal_code = [color for color in self.code_given_in_colors]
        code = [RGB_TO_COLORS[stone.color] for stone in self.current_combination_stones]
        return self.evaluate(code, goal_code)
                    
    
    def _handle_clicked_color_stone(self, clicked_stone):
        if Settings.DEBUG_LEVEL >= 1:
            print 'clicked colored stone: ' + str((clicked_stone, RGB_TO_COLORS[clicked_stone.color]))
            
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
        
    def _draw_result_tuples(self, surface):
        pos_x = surface.get_width() * 0.9
        for i in xrange(len(self.results_tuples)):
            text1 = pygame.font.SysFont('Arial', 24).render(
                str(self.results_tuples[i]),
                True, COLORS_TO_RGB['black'])
            surface.blit(text1, (pos_x, self._get_pos_y_of_combination_stone(surface, i)))
    
    def _init_combinations_matrix(self, round_number, codelength, surface):
        self.combinations_matrix = []
        for j in xrange(Settings.ROUND_NUMBER):
            combination_row = [Stone(COLORS_TO_RGB['black'], BLOCK_SIZE, BLOCK_SIZE,
                                     self._get_pos_x_of_stone(surface, i),
                                     self._get_pos_y_of_combination_stone(surface, j)
                                     )
                               for i in xrange(Settings.CODELENGTH)]
            self.combinations_matrix.append(combination_row)
                                            
        self.current_combination_stones = self.combinations_matrix[0]
        self.selected_combination_stone = self.current_combination_stones[0]
    
    def _get_pos_x_of_stone(self, surface, column_index):    
        return surface.get_width() / (Settings.CODELENGTH + 1) * (column_index + 1) - BLOCK_SIZE / 2
    
    def _get_pos_y_of_combination_stone(self, surface, row_index):
        return (surface.get_height() * 0.8) / Settings.ROUND_NUMBER * row_index + 10
      
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

    def check_is_won(self, result_tuple):
        return True if result_tuple[0] == Settings.CODELENGTH else False

    def check_is_lost(self, current_round):
        return True if current_round == Settings.ROUND_NUMBER else False
