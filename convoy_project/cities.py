# -*- coding: latin1 -*-
'''
Created on May 28, 2018

@author: Jesús Molina
'''

import random


from resources import Resources

class Cities(object):
    '''
    classdocs
    '''


    def __init__(self,town_name="",wood=0,oil=0,water=0,discontent=100):
        '''
        Constructor
        '''
        self.__town_name = town_name
        self.town_resources = Resources(wood,oil,water)
        self.__discontent = discontent
    
    def __str__(self):
        
        data =  "Wood: " + str(self.town_resources.getWood()) \
        + "\n" \
        + "Oil: " + str(self.town_resources.getOil()) \
        + "\n" \
        + "Water: " + str(self.town_resources.getWater()) \
        + "\n" \
        + "Discontent: " +  str(self.__discontent) 
        
        return data
        
        
    def setTownName(self,town_name):
        self.__town_name = town_name
    def getTownName(self):
        return self.__town_name
    
    def setDiscontent(self,discontent):
        self.__discontent = discontent
    def getDiscontent(self):
        return self.__discontent


    def consuming_resources(self):
        
        rate = random.randrange(10, 41) / 100.0
        self.town_resources.setWood(self.town_resources.getWood() - rate)
        self.town_resources.setOil(self.town_resources.getOil() - rate)
    
    def discontent_modifier(self):
        
        if self.town_resources.getWood() <= 0 or self.town_resources.getOil() <= 0:
            self.__discontent -= 1
        if self.__discontent < 1:
            return "gameover"
        
        
        
        