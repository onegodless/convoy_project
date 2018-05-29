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
        self.convoy_defense = convoy_defense #attribute that makes the convoy lose less health in each event.
        self.convoy_running = convoy_running
        self.inst_events = Events()
        self.departure = None #Time when the convoy has to departure from the city.
        self.arrive = None#Time when the convoy comes back.
        self.targeted = 0
    def convoy_is_out(self,game_time):
        
        event = self.inst_events.event_generator(game_time, self.targeted)
        if event == "convoy_lost":
            self.convoy_health -= 30 #defense should be inserted here to damper the damage caused by the event.
            return "convoy_lost"
        elif event == "raiders": 
            self.convoy_health -= 40 #defense should be inserted here to damper the damage caused by the event.
            return "raiders"
        elif event == "sand_storm":
            self.convoy_health -= 20 #defense should be inserted here to damper the damage caused by the event.
            return "sand_storm"
            
    def check_health(self):
        
        if self.convoy_health <= 0:
            return "dead"     