'''
Created on 29.07.2017

@author: Mirco
'''
from util import Settings
from view.CrypterScene import CrypterScene
from view.Stone import Stone
from view.ViewSettings import COLORS_TO_RGB, BLOCK_SIZE

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
        pass
    
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
