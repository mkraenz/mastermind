'''
Created on 10.09.2014

@author: proSingularity
'''
from abc import ABCMeta, abstractmethod

class IPlayerCode(object):

    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_code(self):
        pass

