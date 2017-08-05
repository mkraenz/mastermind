'''
Created on 30.07.2017

@author: Mirco
'''
from view.IScene import IScene
from settings.ViewSettings import COLORS_TO_RGB, BLOCK_SIZE
from view.Stone import Stone
from settings import Settings
import pygame

class CrypterScene(IScene):
    '''
    Contains the common features of EncrypterScene and DecrypterScene
    '''
    def __init__(self, color_choices_stones, code_given_in_colors):
        IScene.__init__(self)
        self.color_choices_stones = color_choices_stones
        self.current_combination_stones = []
        self.code_given_in_colors = code_given_in_colors
        self.selected_combination_stone = None

    def render(self, surface):
        surface.fill(COLORS_TO_RGB['white'])
        self._draw_color_choices(surface, self.color_choices_stones)
        
    def update(self):
        pass
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self._handle_mouse_button_up(self.color_choices_stones,
                                        self.current_combination_stones)
        
    def _draw_color_choices(self, surface, color_choices_stones):
        if not color_choices_stones:
            self.color_choices_stones = self._init_color_choices_stones(surface)
        for stone in self.color_choices_stones:
            stone.render(surface)      

    def _init_color_choices_stones(self, surface):
        counter = 1
        color_choices_stones = []
        for color in Settings.COLORS_TO_NUMBERS:
            stone = Stone(COLORS_TO_RGB[color], BLOCK_SIZE, BLOCK_SIZE,
                          surface.get_width() / (len(Settings.COLORS_TO_NUMBERS) + 1) * counter - BLOCK_SIZE / 2,
                          surface.get_height() * 0.8)
            color_choices_stones.append(stone)
            counter += 1
        return color_choices_stones
    
    
    def _handle_clicked_color_stone(self, clicked_stone):
        raise NotImplementedError
            

    def _handle_mouse_button_up(self, color_choices_stones, combination_stones):
        pos = pygame.mouse.get_pos()
        
        clicked_color_stones = [s for s in color_choices_stones if s.rect.collidepoint(pos)]
        if clicked_color_stones:
            self._handle_clicked_color_stone(clicked_color_stones[0])
            
        else:
            clicked_combination_stones = [s for s in combination_stones if s.rect.collidepoint(pos)]
            if clicked_combination_stones:
                self.selected_combination_stone = clicked_combination_stones[0]
                if Settings.DEBUG_LEVEL >= 1:
                    print('(selected combination stone, index in current_combination_stones) = ',
                          self.selected_combination_stone, self.current_combination_stones.index(self.selected_combination_stone))
        