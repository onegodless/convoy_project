# -*- coding: latin1 -*-
'''
Created on May 28, 2018

@author: Jesús Molina
'''

class Resources(object):
    '''
    classdocs
    '''


    def __init__(self,wood=0,oil=0,water=0):
        '''
        Constructor
        '''
        self.__wood = wood
        self.__oil = oil
        self.__water = water
     
    def __str__(self):
         
        print "Wood: " + str(self.getWood()) +"\n" + "Oil: " + str(self.getOil()) + "\n" + "Water: " +  str(self.getWater())
     
    ####Getters and Setters####
    def setWood(self,wood):
        self.__wood = wood
    def getWood(self):
        return self.__wood

    def setOil(self,oil):
        self.__oil = oil
    def getOil(self):
        return self.__oil
    
    def setWater(self,water):
        self.__water = water
    def getWater(self):
        return self.__water
    
