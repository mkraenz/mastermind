'''
Created on 28.07.2017

@author: Mirco
'''

import pygame
from util import Settings
from ViewSettings import COLORS_TO_RGB
from ViewSettings import BLOCK_SIZE as block_size
from view import ViewSettings

def drawColorChoices(surface, color_choices_stones):
    counter = 1
    for color in Settings.COLORS:
        stone = Stone(COLORS_TO_RGB[color], block_size, block_size,
                      surface.get_width() / (len(Settings.COLORS) + 1) * counter - block_size / 2,
                      surface.get_height() * 0.8)
        surface.blit(stone.image,
            (surface.get_width() / (len(Settings.COLORS) + 1) * counter - block_size / 2,
             surface.get_height() * 0.8))
        color_choices_stones.append(stone)
        counter += 1

def drawRowOfStones(surface, current_row_of_sprites):
    for i in xrange(Settings.STONE_NUMBER):
        stone = Stone(COLORS_TO_RGB['black'],
            block_size, block_size)
        surface.blit(stone.image,
            (surface.get_width() / (Settings.STONE_NUMBER + 1) * (i + 1) - block_size / 2,
            surface.get_height() * 0.4))
        current_row_of_sprites.append(stone)

def handleMouseButtonUp(index_of_block_to_color, color_choices_stones, current_row_of_sprites):
    if len(code_given_in_colors) < Settings.STONE_NUMBER:
        pos = pygame.mouse.get_pos()
        clicked_stones = [s for s in color_choices_stones if s.rect.collidepoint(pos)]
        if clicked_stones:
            clicked_stone = clicked_stones[0]
            if Settings.DEBUG_LEVEL >= 1:
                print(clicked_stone, ViewSettings.RGB_TO_COLORS[clicked_stone.color])
            # TODO: color central stones in color of clicked_stone
            current_row_of_sprites[index_of_block_to_color].set_color(clicked_stone.color)
            pygame.display.update()
    elif True:
        pass  # TODO:
        
class Stone(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, posX=0, posY=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(posX + block_size / 2, posY + block_size / 2))
        
    def set_color(self, color):
        self.color = color
        self.image.fill(color)
        

# main
pygame.init()

surface = pygame.display.set_mode(ViewSettings.SCREEN_DIMENSIONS)
surface.fill(COLORS_TO_RGB['white'])

color_choices_stones = []
current_row_of_sprites = []
code_given_in_colors = []

drawColorChoices(surface, color_choices_stones)
drawRowOfStones(surface, current_row_of_sprites)

gameExit = False
index_of_block_to_color = 0

while not gameExit:
    for event in pygame.event.get():
        if Settings.DEBUG_LEVEL >= 2 and event.type != pygame.MOUSEMOTION:
            print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            handleMouseButtonUp(index_of_block_to_color, color_choices_stones, current_row_of_sprites)
            
        
    pygame.display.update()

pygame.quit()
quit()
