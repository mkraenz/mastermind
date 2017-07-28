'''
Created on 28.07.2017

@author: Mirco
'''

import pygame
from util import Settings
from ViewSettings import COLORS_IN_RGB
from ViewSettings import BLOCK_SIZE as block_size
from view import ViewSettings
from cmath import rect

color_choices_sprites = []
current_row_of_sprites = []

def drawColorChoices(surface):
    counter = 1
    for color in Settings.COLORS:
        rect = pygame.draw.rect(surface, COLORS_IN_RGB[color],
            [surface.get_width() / (len(Settings.COLORS) + 1) * counter - block_size/2,
             surface.get_height() * 0.8, block_size, block_size])
        color_choices_sprites.append(rect)
        counter += 1

def drawRowOfEmptyRectangles(surface):
    counter = 1
    for i in xrange(Settings.STONE_NUMBER):
        rect = pygame.draw.rect(surface, COLORS_IN_RGB['black'],
            [surface.get_width() / (Settings.STONE_NUMBER + 1) * counter - block_size/2,
             surface.get_height() * 0.4, block_size, block_size])
        current_row_of_sprites.append(rect)
        counter += 1

def handleMouseButtonUp():
    pos = pygame.mouse.get_pos()
    clicked_sprites = [s for s in color_choices_sprites if s.collidepoint(pos)]
    if clicked_sprites:
        clicked_sprite = clicked_sprites[0]
        print(clicked_sprite)



# main
pygame.init()

surface = pygame.display.set_mode(ViewSettings.SCREEN_DIMENSIONS)
surface.fill(COLORS_IN_RGB['white'])
drawColorChoices(surface)
drawRowOfEmptyRectangles(surface)

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if Settings.DEBUG_LEVEL >= 2 and event.type != pygame.MOUSEMOTION:
            print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:
            handleMouseButtonUp()
            
        
    pygame.display.update()

pygame.quit()
quit()
