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


    def __init__(self,convoy_name="",convoy_health=100,num_escorts=0):
        '''
        Constructor
        '''
        self.convoy_name= convoy_name
        self.convoy_health = convoy_health
        self.convoy_defense = 0 #attribute that makes the convoy lose less health in each event.
        self.convoy_running = 0
        self.inst_events = Events()
        self.departure = None #Time when the convoy has to departure from the city.
        self.arrive = None#Time when the convoy comes back.
        self.targeted = 0
        self.__num_trucks = 0
        self.__num_escort = num_escorts
        self.__max_number = 20
        self.calculate_defense()
        
    
    def __str__(self):
        
        return "data: " + str(self.__num_escort) + str(self.convoy_defense)
    
    def set_num_trucks(self, num_trucks):
        self.__num_trucks = num_trucks
    def get_num_trucks(self):
        return self.__num_trucks
    def set_num_escort(self,num_escort):
        self.__num_escort = num_escort
    def get_num_escort(self):
        return self.__num_escort
    def get_max_number(self):
        return self.__max_number
        
        
    def convoy_is_out(self,game_time):
        
        print "defense : " + str(self.convoy_defense)
        event = self.inst_events.event_generator(game_time, self.targeted)
        if event == "convoy_lost":
            self.convoy_health -= 30 - self.convoy_defense#defense should be inserted here to damper the damage caused by the event.
            return "convoy_lost"
        elif event == "raiders": 
            self.convoy_health -= 40 - self.convoy_defense#defense should be inserted here to damper the damage caused by the event.
            return "raiders"
        elif event == "sand_storm":
            self.convoy_health -= 25 - self.convoy_defense#defense should be inserted here to damper the damage caused by the event.
            return "sand_storm"
            
            
    def check_health(self):
        
        if self.convoy_health <= 0:
            return "dead"  
    
    
    def calculate_defense(self):
        
        self.convoy_defense = self.__num_escort * 2
        