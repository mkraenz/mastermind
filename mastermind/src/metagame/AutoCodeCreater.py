'''
Created on 05.08.2017

@author: Mirco
'''
from random import randint
from settings import Settings

class AutoCodeCreater(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def get_code(self):
        code_in_numbers = [randint(1, len(Settings.COLORS_TO_NUMBERS)) for _ in xrange(Settings.CODELENGTH)]
        return [Settings.NUMBERS_TO_COLORS[x] for x in code_in_numbers]