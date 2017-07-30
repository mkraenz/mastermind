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

    def update(self):
        pass

    def render(self, surface):
        surface.fill(COLORS_TO_RGB['white'])
        self._draw_color_choices(surface, self.color_choices_stones)
        
    def _draw_color_choices(self, surface, color_choices_stones):
        if not color_choices_stones:
            self.color_choices_stones = self._init_color_choices_stones(surface)
        for stone in self.color_choices_stones:
            stone.render(surface)      

    def _init_color_choices_stones(self, surface):
        counter = 1
        color_choices_stones = []
        for color in Settings.COLORS:
            stone = Stone(COLORS_TO_RGB[color], BLOCK_SIZE, BLOCK_SIZE,
                          surface.get_width() / (len(Settings.COLORS) + 1) * counter - BLOCK_SIZE / 2,
                          surface.get_height() * 0.8)
            color_choices_stones.append(stone)
            counter += 1
        return color_choices_stones