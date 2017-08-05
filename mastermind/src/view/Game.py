'''
Created on 28.07.2017

@author: Mirco
'''

import pygame
from settings.ViewSettings import COLORS_TO_RGB
from settings import ViewSettings
from view.SceneManager import SceneManager
import sys
from pygame.constants import VIDEORESIZE

def game_loop(surface):
    game_running = True
    manager = SceneManager()
    clock = pygame.time.Clock()
    
    while game_running:
        if pygame.event.get(pygame.QUIT):
            game_running = False
            return
        for event in pygame.event.get(VIDEORESIZE):
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(surface)
        pygame.display.update()
        clock.tick(60)
    
def getConfiguredMainSurface():
    surface = pygame.display.set_mode(ViewSettings.SCREEN_DIMENSIONS, pygame.RESIZABLE)
    surface.fill(COLORS_TO_RGB['white'])
    pygame.display.set_caption('Mastermind. App by ProSingularity.')
    return surface

def main():
        
    pygame.init()
    surface = getConfiguredMainSurface()
    game_loop(surface)
    pygame.quit()
    sys.exit()
    
main()