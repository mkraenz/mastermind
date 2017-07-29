'''
Created on 29.07.2017

@author: Mirco
'''
from view.IScene import IScene
import pygame
from util import Settings
from view import ViewSettings
from view.ViewSettings import COLORS_TO_RGB
from view.Stone import Stone
from ViewSettings import BLOCK_SIZE


class EncrypterScene(IScene):
    
    def __init__(self, color_choices_stones, current_row_of_stones, code_given_in_colors):
        IScene.__init__(self)
        self.color_choices_stones = color_choices_stones
        self.current_row_of_stones = current_row_of_stones
        self.code_given_in_colors = code_given_in_colors
        
        if Settings.DEBUG_LEVEL >= 1:
            print('enter EncrypterScene')
            
    def render(self, surface):
        if not self.current_row_of_stones:
            self.current_row_of_stones = self._init_current_row_of_stones(surface)
        surface.fill(COLORS_TO_RGB['white'])
        self.drawColorChoices(surface, self.color_choices_stones)
        self.drawRowOfStones(surface, self.current_row_of_stones)
#         for stone in self.current_row_of_stones:
#             stone.render(surface)

    def _init_current_row_of_stones(self, surface):
        return [Stone(COLORS_TO_RGB['black'], BLOCK_SIZE, BLOCK_SIZE,
                surface.get_width() / (Settings.STONE_NUMBER + 1) * (i + 1) - BLOCK_SIZE / 2,
                surface.get_height() * 0.4) 
                                            for i in xrange(Settings.STONE_NUMBER)]
    
    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self._handle_mouse_button_up(self.code_given_in_colors, self.color_choices_stones, 
                                        self.current_row_of_stones)


    def _handle_mouse_button_up(self, code_given_in_colors, color_choices_stones, current_row_of_sprites):
        if len(code_given_in_colors) < Settings.STONE_NUMBER:
            pos = pygame.mouse.get_pos()
            clicked_stones = [s for s in color_choices_stones if s.rect.collidepoint(pos)]
            if clicked_stones:
                clicked_stone = clicked_stones[0]
                if Settings.DEBUG_LEVEL >= 1:
                    print('clicked colored stone: ' + 
                          str((clicked_stone, ViewSettings.RGB_TO_COLORS[clicked_stone.color])))
                # TODO: color central stones in color of clicked_stone
                self.current_row_of_stones[len(code_given_in_colors)].set_color(clicked_stone.color)
                # pygame.display.update()
                
                code_given_in_colors.append(ViewSettings.RGB_TO_COLORS[clicked_stone.color])
                if Settings.DEBUG_LEVEL >= 1:
                    print('code_given_in_colors = ' + str(code_given_in_colors))
                
        elif True:
            pass  # TODO:
        
        
    def drawColorChoices(self, surface, color_choices_stones):
        counter = 1
        for color in Settings.COLORS:
            stone = Stone(COLORS_TO_RGB[color], BLOCK_SIZE, BLOCK_SIZE,
                          surface.get_width() / (len(Settings.COLORS) + 1) * counter - BLOCK_SIZE / 2,
                          surface.get_height() * 0.8)
            surface.blit(stone.image,
                (surface.get_width() / (len(Settings.COLORS) + 1) * counter - BLOCK_SIZE / 2,
                surface.get_height() * 0.8))
            color_choices_stones.append(stone)
            counter += 1
    
    def drawRowOfStones(self, surface, current_row_of_sprites):
        for stone in current_row_of_sprites:
            stone.render(surface)
