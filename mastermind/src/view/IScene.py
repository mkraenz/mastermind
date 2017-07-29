'''
Created on 29.07.2017

@author: Mirco
'''
class IScene(object):
    def __init__(self):
        pass

    def render(self, surface):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError