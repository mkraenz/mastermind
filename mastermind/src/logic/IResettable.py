'''
Created on 28.07.2017

@author: Mirco
'''

from abc import ABCMeta, abstractmethod

class IResettable(object):
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def reset(self):
        pass
    

