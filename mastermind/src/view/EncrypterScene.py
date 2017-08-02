'''
Created on 29.07.2017

@author: Mirco
'''
import pygame
from util import Settings
from view.ViewSettings import COLORS_TO_RGB
from view.Stone import Stone
from ViewSettings import BLOCK_SIZE
from view.DecrypterScene import DecrypterScene
from view.CrypterScene import CrypterScene
from view import ViewSettings


class EncrypterScene(CrypterScene):
    
    def __init__(self, color_choices_stones, code_given_in_colors):
        CrypterScene.__init__(self, color_choices_stones, code_given_in_colors)
        
        if Settings.DEBUG_LEVEL >= 1:
            print('enter EncrypterScene')
            
    def render(self, surface):
        CrypterScene.render(self, surface)
        self._draw_row_of_stones(surface, self.current_combination_stones)
        if self.code_given_in_colors.count('') == 0:
            self.draw_continue_text(surface)


    def handle_events(self, events):
        CrypterScene.handle_events(self, events)
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN and \
                        self._is_valid_combination(self.current_combination_stones):
                self.manager.go_to(DecrypterScene(self.color_choices_stones, self.code_given_in_colors))
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.manager.go_to(DecrypterScene(self.color_choices_stones, ['red']*Settings.CODELENGTH))



    def draw_continue_text(self, surface):
        text1 = pygame.font.SysFont('Arial', 24).render(
            'This is the goal combination. Press Return key to continue.',
            True, COLORS_TO_RGB['black'])
        surface.blit(text1, (120, 200))
        
    def _draw_row_of_stones(self, surface, current_row_of_sprites):
        if not self.current_combination_stones:
            self._init_current_row_of_stones(surface)
            self._init_code_given_in_colors()
        for stone in current_row_of_sprites:
            stone.render(surface)

    def _init_current_row_of_stones(self, surface):
        self.current_combination_stones = [Stone(COLORS_TO_RGB['black'], BLOCK_SIZE, BLOCK_SIZE,
                surface.get_width() / (Settings.CODELENGTH + 1) * (i + 1) - BLOCK_SIZE / 2,
                surface.get_height() * 0.4) 
                                            for i in xrange(Settings.CODELENGTH)]
        self.selected_combination_stone = self.current_combination_stones[0]
        
    def _init_code_given_in_colors(self):
        self.code_given_in_colors = [''] * Settings.CODELENGTH

    def _is_valid_combination(self, combination):
        black_stones = [stone for stone in combination if stone.color == COLORS_TO_RGB['black']]
        return True if not black_stones else False
    
    def _handle_clicked_color_stone(self, clicked_stone):
        if Settings.DEBUG_LEVEL >= 1:
            print 'clicked colored stone: ' + str((clicked_stone, ViewSettings.RGB_TO_COLORS[clicked_stone.color]))
            
        self.selected_combination_stone.set_color(clicked_stone.color)
        index = self.current_combination_stones.index(self.selected_combination_stone)
        self.code_given_in_colors[index] = ViewSettings.RGB_TO_COLORS[clicked_stone.color]
        
        if Settings.DEBUG_LEVEL >= 1:
            print 'code_given_in_colors = ' + str(self.code_given_in_colors)
