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


    def __init__(self,name="",health=100,num_escorts=0):
        '''
        Constructor
        '''
        self.name= name
        self.health = health
        self.defense = 0 #attribute that makes the convoy lose less health in each event.
        self.__running = 0
        self.inst_events = Events()
        self.__departure = None #Time when the convoy has to departure from the city.
        self.__arrive = None#Time when the convoy comes back.
        self.__targeted = 0
        self.__num_trucks = 0
        self.__num_escort = num_escorts
        self.__max_number = 20
        self.calculate_defense()
        
    
    def __str__(self):
        
        return "data: " + str(self.__num_escort) + str(self.defense)
    
    def set_running(self,running):
        self.__running = running
    def get_running(self):
        return self.__running
    def set_arrive(self,arrive):
        self.__arrive = arrive
    def get_arrive(self):
        return self.__arrive
    def set_departure(self,departure):
        self.__departure = departure
    def get_departure(self):
        return self.__departure
    def set_targeted(self,targeted):
        self.__targeted = targeted
    def get_targeted(self):
        return self.__targeted
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
        
        event = self.inst_events.event_generator(game_time, self.__targeted)
        if event == "convoy_lost":
            self.health -= 30 - self.defense#defense should be inserted here to damper the damage caused by the event.
            return "convoy_lost"
        elif event == "raiders": 
            self.health -= 40 - self.defense#defense should be inserted here to damper the damage caused by the event.
            return "raiders"
        elif event == "sand_storm":
            self.health -= 25 - self.defense#defense should be inserted here to damper the damage caused by the event.
            return "sand_storm"
            
            
    def check_health(self):
        
        if self.health <= 0:
            return "dead"  
    
    
    def calculate_defense(self):
        
        self.defense = self.__num_escort * 2
        