'''
Created on 10.09.2014

@author: proSingularity
'''
from abc import ABCMeta, abstractmethod

class IWinManager(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def is_won(self):
        pass
    
    @abstractmethod
    def is_lost(self):
        pass
    
