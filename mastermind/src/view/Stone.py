'''
Created on 29.07.2017

@author: Mirco
'''
import pygame
from ViewSettings import BLOCK_SIZE as block_size
 
class Stone(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(posX + block_size / 2, posY + block_size / 2))
        
    def render(self, surface):
        self.rect = pygame.draw.rect(surface, self.color, self.rect)
        
    def set_color(self, color):
        self.color = color
