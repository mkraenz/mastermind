'''
Created on 29.07.2017

@author: Mirco
'''
import pygame
from view import ViewSettings
from view.IScene import IScene
from view.ViewSettings import COLORS_TO_RGB
from view.EncrypterScene import EncrypterScene
from util import Settings

class TitleScene(IScene):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 50)
        self.sfont = pygame.font.SysFont('Arial', 32)
        
        self.start_game_text_rect = None
        self.exit_game_text_rect = None
        
        if Settings.DEBUG_LEVEL >= 1:
            print('enter TitleScene')


    def _draw_start_new_game_button(self, surface):
        start_game_text = self.font.render('Start new game.', True, COLORS_TO_RGB['black'])
        self.start_game_text_rect = start_game_text.get_rect(center=(surface.get_width() / 2, 350))
        pygame.draw.rect(surface, COLORS_TO_RGB['green'], self.start_game_text_rect, 5)
        surface.blit(start_game_text, self.start_game_text_rect)


    def _draw_exit_game_button(self, surface):
        exit_game_text = self.font.render('Quit game.', True, COLORS_TO_RGB['black'])
        self.exit_game_text_rect = exit_game_text.get_rect(center=(surface.get_width() / 2, 450))
        pygame.draw.rect(surface, COLORS_TO_RGB['green'], self.exit_game_text_rect, 5)
        surface.blit(exit_game_text, self.exit_game_text_rect)

    def _draw_title(self, surface):
        title_text = self.font.render('Are you the Mastermind?', True, COLORS_TO_RGB['black'])
        surface.blit(title_text, (200, 50))

    def render(self, surface):
        surface.fill(ViewSettings.COLORS_TO_RGB['white'])
        self._draw_title(surface)
        self._draw_start_new_game_button(surface)
        self._draw_exit_game_button(surface)

    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.start_game_text_rect.collidepoint(pos):
                    self.manager.go_to(EncrypterScene([], []))
                elif self.exit_game_text_rect.collidepoint(pos):
                    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
