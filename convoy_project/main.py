# -*- coding: latin1 -*-

'''
Created on May 28, 2018

@author: Jes�s Molina
'''

import time

from cities import Cities
from convoy_control import ConvoyControl

if __name__ == '__main__':
    
    game_time = 12
    main_city = Cities("Nuka Town",20,20,20,100) #wood, oil, water, discontent.
    my_convoy_control = ConvoyControl()
    my_convoy_control.create_convoy("Slipknot",100,10) #name, health, number of escorts.
    my_convoy_control.create_convoy("Slayer",100, 5)
    my_convoy_control.set_convoy_times("Slipknot",13,12)
    
    while True:
        
        print "\n"
        print "Time: " + str(game_time) + ":00"
        print "\n" 
        
        my_convoy_control.time_control(game_time)

        print main_city
        main_city.consuming_resources()
        if main_city.discontent_modifier() == "gameover":
            print "Game Over. You ran out of resources for too long."
            break
        game_time += 1
        if game_time == 24:
            game_time = 0
        time.sleep(1)