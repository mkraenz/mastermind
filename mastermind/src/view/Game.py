'''
Created on 28.07.2017

@author: Mirco
'''

import pygame
from ViewSettings import COLORS_TO_RGB
from view import ViewSettings
from view.SceneManager import SceneManager

def game_loop(surface):
    game_running = True
    manager = SceneManager()
    
    while game_running:
        if pygame.event.get(pygame.QUIT):
            game_running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(surface)
        pygame.display.update()
    
def getConfiguredMainSurface():
    surface = pygame.display.set_mode(ViewSettings.SCREEN_DIMENSIONS)
    surface.fill(COLORS_TO_RGB['white'])
    pygame.display.set_caption('Mastermind. App by ProSingularity.')
    return surface

def main():
    pygame.init()
    surface = getConfiguredMainSurface()
    game_loop(surface)
    pygame.quit()
    quit()
    
main()