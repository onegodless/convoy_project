# -*- coding: latin1 -*-

'''
Created on May 28, 2018

@author: Jesús Molina
'''

import time

from cities import Cities

if __name__ == '__main__':
    
    game_time = 12
    main_city = Cities("Nuka Town",0,20,20,3)
    
    while True:
        
        print main_city
        main_city.consuming_resources()
        if main_city.discontent_modifier() == "gameover":
            print "Game Over. You ran out of resources for too long."
            break
        game_time += 1
        time.sleep(3)