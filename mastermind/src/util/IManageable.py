'''
Created on 10.09.2014

@author: proSingularity
'''
from abc import ABCMeta, abstractmethod

class IManageable(object):
    '''
    classdocs
    '''
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def manage(self):
        pass