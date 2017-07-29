'''
Created on 29.07.2017

@author: Mirco
'''
from view.IScene import IScene
from view.ViewSettings import COLORS_TO_RGB

class DecrypterScene(IScene):
    
    def __init__(self):
        print('Enter DecrypterScene')
        pass

    def render(self, surface):
        surface.fill(COLORS_TO_RGB['white'])
        pass

    def update(self):
        pass

    def handle_events(self, events):
        pass