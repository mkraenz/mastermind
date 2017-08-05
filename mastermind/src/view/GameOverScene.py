'''
Created on 02.08.2017

@author: Mirco
'''
import pygame
from settings import ViewSettings
from settings.ViewSettings import COLORS_TO_RGB
from view.IScene import IScene

class GameOverScene(IScene):
    
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 50)

    def render(self, surface):
        surface.fill(ViewSettings.COLORS_TO_RGB['white'])
        self.draw_centered_text('Game Over. Better try again.', 200, surface)
        self.draw_centered_text('Click to return to title screen.', 400, surface)

    def draw_centered_text(self, message, height, surface):
        text = self.font.render(message, True, COLORS_TO_RGB['black'])
        text_rect = text.get_rect(center=(surface.get_width() / 2, height))
        surface.blit(text, text_rect)
        
    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.manager.new_game()
