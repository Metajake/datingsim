from getinputobject import *
from location_definitions import *
from girl_definitions import *
from elements import *

e = Engine()
i = Input()
mc = Character()
e.build_locations(location_list)
e.build_girls(girl_list)

s1 = Scene(e.current_location, e.girls['tammy'])

##### Begin game ######
e.introduction()
mc.get_name()
e.activate_location('home_exterior', i, mc)

while e.game_over != True:
    #print i.verb
    #print i.direction
    #print i.noun
    
    e.get_input(i, mc)