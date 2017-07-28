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

def drawColorChoices():
    counter = 1
    for color in Settings.COLORS:
        rect = pygame.draw.rect(screen, COLORS_IN_RGB[color],
            [screen.get_width() / (len(Settings.COLORS) + 1) * counter - block_size/2,
             screen.get_height() * 0.8, block_size, block_size])
        color_choices_sprites.append(rect)
        counter += 1

def drawRowOfEmptyRectangles():
    counter = 1
    for i in xrange(Settings.STONE_NUMBER):
        rect = pygame.draw.rect(screen, COLORS_IN_RGB['black'],
            [screen.get_width() / (len(Settings.COLORS) + 1) * counter - block_size/2,
             screen.get_height() * 0.8, block_size, block_size])
        current_row_of_sprites.append(rect)
        counter += 1

pygame.init()

screen = pygame.display.set_mode(ViewSettings.SCREEN_DIMENSIONS)
screen.fill(COLORS_IN_RGB['white'])
drawColorChoices()

clock = pygame.time.Clock()

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type != pygame.MOUSEMOTION:
            print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprite = [s for s in color_choices_sprites if s.collidepoint(pos)][0]
            print(clicked_sprite)
            
        
    pygame.display.update()

pygame.quit()
quit()
