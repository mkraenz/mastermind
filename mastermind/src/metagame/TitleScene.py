'''
Created on 29.07.2017

@author: Mirco
'''
import pygame
from settings import ViewSettings
from gamemanagement.IScene import IScene
from settings.ViewSettings import COLORS_TO_RGB
from settings import Settings
from gamemanagement.AutoCodeCreater import AutoCodeCreater
from ingame.EncrypterScene import EncrypterScene
from ingame.DecrypterScene import DecrypterScene

class TitleScene(IScene):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 50)
        self.sfont = pygame.font.SysFont('Arial', 32)
        
        self.start_multiplayer_game_text_rect = None
        self.start_singleplayer_game_text_rect = None
        self.exit_game_text_rect = None
        
        if Settings.DEBUG_LEVEL >= 1:
            print('enter TitleScene')


    def _draw_start_multiplayer_game_button(self, surface):
        multiplayer_game_text = self.font.render(' 2 Players ', True, COLORS_TO_RGB['black'])
        self.start_multiplayer_game_text_rect = multiplayer_game_text.get_rect(center=(surface.get_width() / 2, 400))
        self._draw_text_button(surface, multiplayer_game_text, self.start_multiplayer_game_text_rect)


    def _draw_text_button(self, surface, text, text_rect):
        pygame.draw.rect(surface, COLORS_TO_RGB['green'], text_rect, 5)
        surface.blit(text, text_rect)

    def _draw_start_singleplayer_game_button(self, surface):
        start_game_text = self.font.render(' 1 Player ', True, COLORS_TO_RGB['black'])
        self.start_singleplayer_game_text_rect = start_game_text.get_rect(center=(surface.get_width() / 2, 325))
        self._draw_text_button(surface, start_game_text, self.start_singleplayer_game_text_rect)

    def _draw_exit_game_button(self, surface):
        exit_game_text = self.font.render(' Quit game ', True, COLORS_TO_RGB['black'])
        self.exit_game_text_rect = exit_game_text.get_rect(center=(surface.get_width() / 2, 475))
        self._draw_text_button(surface, exit_game_text, self.exit_game_text_rect)

    def _draw_title(self, surface):
        title_text = self.font.render('Are you the Mastermind?', True, COLORS_TO_RGB['black'])
        title_text_rect = title_text.get_rect(center=(surface.get_width()/2, 100))
        surface.blit(title_text, title_text_rect)

    def render(self, surface):
        surface.fill(ViewSettings.COLORS_TO_RGB['white'])
        self._draw_title(surface)
        self._draw_start_singleplayer_game_button(surface)
        self._draw_start_multiplayer_game_button(surface)
        self._draw_exit_game_button(surface)

    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                if self.start_singleplayer_game_text_rect.collidepoint(pos):
                    code_given_in_colors = AutoCodeCreater().get_code()
                    if Settings.DEBUG_LEVEL >= 1:
                        print(code_given_in_colors)
                    self.manager.go_to(DecrypterScene([], code_given_in_colors))
                    
                elif self.start_multiplayer_game_text_rect.collidepoint(pos):
                    self.manager.go_to(EncrypterScene([], []))
                    
                elif self.exit_game_text_rect.collidepoint(pos):
                    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
