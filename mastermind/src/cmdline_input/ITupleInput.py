'''
Created on 10.09.2014

@author: proSingularity
'''
from abc import ABCMeta, abstractmethod

class ITupleInput(object):
    '''
    classdocs
    '''

    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_tuple(self):
        '''
        @return: The combination given to the command line, if it is valid, else None.
        '''
        pass