# -*- coding: latin1 -*-

'''
Created on May 28, 2018

@author: Jesús Molina
'''

from convoy import Convoy
from convoy_project import convoy


class ConvoyControl(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.list_convoys = []
    
    
    def time_control(self,game_time):
        '''time_control gets the game_time of each main cicle and compares it 
        to time that the convoys on the list are supposed to head out or come
        back to the city.
        when a convoy is out, this function also checks if the convoys encounter
        an event.
        '''
        for convoy in self.list_convoys:
            if convoy.get_departure() == game_time:  
                convoy.set_running(1)
                print "The convoy " + str(convoy.name) + " heads out."
                                     
            elif convoy.get_arrive() == game_time and convoy.get_running() == 1:
                print "The convoy " + str(convoy.name) + " came back."
                convoy.set_running(0)
                convoy.set_departure(None)
                convoy.set_arrive(None)
                convoy.set_targeted(0)
            
            elif convoy.get_running() == 1:
                run = convoy.convoy_is_out(game_time)
                
                if run == "convoy_lost" or run == "sand_storm" or run == "raiders":
                    self.event_convoy(convoy,run)
                    
                if convoy.check_health() == "dead":
                    self.dead_convoy(convoy) 
                
    
    def create_convoy(self,name,health,num_escort):
        '''
        creates a convoy object and push it into the list
        '''    
        new_convoy = Convoy(name,health,num_escort)
        self.list_convoys.append(new_convoy)
    
    def dead_convoy(self,convoy):
        '''
        checks the health of the convoy, if it's dead, pops it out of the
        list.
        '''
        dead_convoy = self.list_convoys.pop()
        print "the convoy" + dead_convoy.name +  " is dead"
    
    def event_convoy(self,convoy,event):
        '''
        prints the convoy's health.
        '''
        convoy.set_targeted(convoy.get_targeted() + 1) 
        print "The convoy has encounter an event: " + str(event) + "."
        print "Convoy " + str(convoy.name) + " has " + str(convoy.health) + " points of health."
    
    
    def set_convoy_times(self,name,departure,arrive):
        
        for convoy in self.list_convoys:
            if convoy.name == name:
                convoy.set_departure(departure)
                convoy.set_arrive(arrive)