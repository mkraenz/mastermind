'''
Created on 02.08.2017

@author: Mirco
'''
from view.IScene import IScene
from view.ViewSettings import COLORS_TO_RGB
from view import ViewSettings
import pygame

class WinScene(IScene):
    
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 50)

    def render(self, surface):
        surface.fill(ViewSettings.COLORS_TO_RGB['white'])
        text1 = self.font.render('You win! Congratulations.', True, COLORS_TO_RGB['black'])
        text2 = self.font.render('Press Return to start a new game.', True, COLORS_TO_RGB['black'])
        surface.blit(text1, (200, 50))
        surface.blit(text2, (200, 350))
        
    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
#                 self.manager.go_to(EncrypterScene([],[]))
                self.manager.new_game()
                print('goto EncrypterScene')