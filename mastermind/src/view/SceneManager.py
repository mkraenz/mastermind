'''
Created on 29.07.2017

@author: Mirco
'''
from view.TitleScreen import TitleScene

class SceneManager(object):
    
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self