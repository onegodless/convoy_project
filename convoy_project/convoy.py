# -*- coding: latin1 -*-
'''
Created on May 28, 2018

@author: Jesús Molina
'''

from events import Events

class Convoy(object):
    '''
    classdocs
    '''


    def __init__(self,convoy_name="",convoy_health=100,convoy_defense=100,convoy_running=0):
        '''
        Constructor
        '''
        self.convoy_name= convoy_name
        self.convoy_health = convoy_health
        self.convoy_defense = convoy_defense
        self.convoy_running = convoy_running
        self.inst_events = Events()
        self.departure = None
        self.arrive = None
    
    def convoy_is_out(self,game_time):
        
        event = self.inst_events.event_generator(game_time)
        if event == "convoy_lost":
            self.convoy_health -= 30
            return "convoy_lost"
        elif event == "raiders": 
            self.convoy_health -= 40
            return "raiders"
        elif event == "sand_storm":
            self.convoy_health -= 20
            return "raiders"
            
    def check_health(self):
        
        if self.convoy_health <= 0:
            return "dead"     