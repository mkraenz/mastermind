'''
Created on 29.07.2017

@author: Mirco
'''
import pygame
from view import ViewSettings
from view.IScene import IScene
from view.ViewSettings import COLORS_TO_RGB
from view.EncrypterScene import EncrypterScene
class TitleScene(IScene):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 50)
        self.sfont = pygame.font.SysFont('Arial', 32)

    def render(self, surface):
        surface.fill(ViewSettings.COLORS_TO_RGB['white'])
        text1 = self.font.render('Are you the Mastermind?', True, COLORS_TO_RGB['black'])
        text2 = self.font.render('Hit Return to Start', True, COLORS_TO_RGB['black'])
        surface.blit(text1, (200, 50))
        surface.blit(text2, (200, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                self.manager.go_to(EncrypterScene([], [], []))
