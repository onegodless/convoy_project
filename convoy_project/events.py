# -*- coding: latin1 -*-
'''
Created on May 28, 2018

@author: Jesús Molina
'''
import random

class Events(object):
    '''Events can be things like the convoy getting lost, attacked by 
    raiders or be engulfed by a sandstorm.
    The hour of the day makes an event be more probable than other. i.e.,
    the convoy can get lost more easily at night.'''


    def __init__(self):
        '''
        Constructor
        '''
    
    def event_generator(self,game_time,targeted):
        
        dictionary_events = {'convoy_lost': 0, 'raiders': 0, 'sand_storm': 0}
        convoy_lost_probability = 0 #initializing variable.
        raiders_probability = 0 #initializing variable.
        sand_storm_probability = 0 #initializing variable.
        
        if game_time > 20 and game_time < 6: #at night is more probable for the convoy to get lost.
            convoy_lost_probability = 40
            raiders_probability = 10
            sand_storm_probability = 10
            
        elif game_time > 5 and game_time < 21:#at day is more probable for the convoy to get attacked or engulfed in a sandstorm.
            convoy_lost_probability = 10
            raiders_probability = 20
            sand_storm_probability = 40
         
        event_happens = random.randint(0,targeted + 5) 
        if event_happens >= 0 and event_happens <= 2:
            dictionary_events["convoy_lost"] = (random.randrange(10, 41, 10) + convoy_lost_probability)
            dictionary_events["raiders"] = (random.randrange(10, 41, 10) + raiders_probability)
            dictionary_events["sand_storm"] = (random.randrange(10, 41, 10) + sand_storm_probability)
            
            maxEvent = max(dictionary_events, key=dictionary_events.get) #gets the element of the dictionary with the higher value.
            return maxEvent #returns the event that has happend.
        
        else:
            pass #no event happens.