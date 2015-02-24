from getinputobject import *
from location_definitions import *
from girl_definitions import *
from elements import *

e = Engine()
i = Input()
mc = Character("J")
e.build_locations(location_list)
e.build_girls(girl_list)

e.activate_location('home_exterior', i, mc)

while e.game_over != True:
    #print i.verb
    #print i.direction
    e.get_input(i, mc)