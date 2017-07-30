'''
Created on 29.07.2017

@author: Mirco
'''
from util import Settings
from view.CrypterScene import CrypterScene

class DecrypterScene(CrypterScene):
    
    def __init__(self, color_choices_stones, code_given_in_colors):
        CrypterScene.__init__(self, color_choices_stones, code_given_in_colors)
        if Settings.DEBUG_LEVEL >= 1:
            print('Enter DecrypterScene')

    def render(self, surface):
        CrypterScene.render(self, surface)
        self._draw_row_of_stones(surface, self.current_combination_stones)

    def update(self):
        pass

    def handle_events(self, events):
        pass
    
    def _draw_row_of_stones(self, surface, current_row_of_sprites):
        if not self.current_combination_stones:
            self._init_current_row_of_stones(surface)
            self._init_code_given_in_colors()
        for stone in current_row_of_sprites:
            stone.render(surface)
            
