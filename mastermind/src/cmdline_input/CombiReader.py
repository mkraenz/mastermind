'''
Created on 04.09.2014

@author: proSingularity
'''

from model.Settings import COLORS as COLORS

class CombiReader(object):
    '''
    classdocs
    '''


    def read_cmd(self):
        '''
        @return: The combination given to the command line, if it is valid, else None.
        '''
        incoming = raw_input("Please insert your combination, e.g. 'red blue yellow pink blue':\n")
        try:
            incoming_list = incoming.split()
            # consistency test
            combi = [COLORS[color] for color in incoming_list]
            return combi
        except: KeyError("Non-valid value found.")
        finally:
            pass
        return None
            
