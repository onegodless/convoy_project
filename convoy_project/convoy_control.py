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
        
        for convoy in self.list_convoys:
            if convoy.departure == game_time:  
                run = convoy.convoy_is_out(game_time)
                convoy.convoy_running = 1
                print "The convoy " + str(convoy.convoy_name) + " heads out."
                
                if run == "convoy_lost" or run == "sand_storm" or run =="raiders":
                    self.event_convoy(convoy,run)
                
                if convoy.check_health() == "dead":
                    self.dead_convoy(convoy)
                     
            elif convoy.arrive == game_time:
                print "The convoy " + str(convoy.convoy_name) + " came back."
                convoy.convoy_running = 0
                convoy.departure = None
                convoy.arrive = None
            
            elif convoy.convoy_running == 1:
                run = convoy.convoy_is_out(game_time)
                
                if run == "convoy_lost" or run == "sand_storm" or run == "raiders":
                    self.event_convoy(convoy,run)
                    
                if convoy.check_health() == "dead":
                    self.dead_convoy(convoy) 
                
    
    def create_convoy(self,name,health,defense):
        
        new_convoy = Convoy(name,health,defense)
        self.list_convoys.append(new_convoy)
    
    def dead_convoy(self,convoy):
        
        dead_convoy = self.list_convoys.pop()
        print "the convoy" + dead_convoy.convoy_name +  " is dead"
    
    def event_convoy(self,convoy,event):
        print "The convoy has encounter an event."
        print str(convoy.convoy_health)