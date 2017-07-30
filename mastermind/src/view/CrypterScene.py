'''
Created on 30.07.2017

@author: Mirco
'''
from view.IScene import IScene
from view.ViewSettings import COLORS_TO_RGB, BLOCK_SIZE
from view.Stone import Stone
from util import Settings

class CrypterScene(IScene):
    '''
    classdocs
    '''
    def __init__(self, color_choices_stones, code_given_in_colors):
        IScene.__init__(self)
        self.color_choices_stones = color_choices_stones
        self.current_combination_stones = []
        self.code_given_in_colors = code_given_in_colors
        self.selected_combination_stone = None


    def render(self, surface):
        surface.fill(COLORS_TO_RGB['white'])
        if not self.current_combination_stones:
            self._init_current_row_of_stones(surface)
        self._draw_color_choices(surface, self.color_choices_stones)
        
    def _draw_color_choices(self, surface, color_choices_stones):
        if not color_choices_stones:
            self.color_choices_stones = self._init_color_choices_stones(surface)
        for stone in self.color_choices_stones:
            stone.render(surface)      

    def _init_current_row_of_stones(self, surface):
        self.current_combination_stones = [Stone(COLORS_TO_RGB['black'], BLOCK_SIZE, BLOCK_SIZE,
                surface.get_width() / (Settings.STONE_NUMBER + 1) * (i + 1) - BLOCK_SIZE / 2,
                surface.get_height() * 0.4) 
                                            for i in xrange(Settings.STONE_NUMBER)]
        self.selected_combination_stone = self.current_combination_stones[0]
