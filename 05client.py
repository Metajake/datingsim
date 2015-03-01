from engine_text import *
from getinputobject import *
from getdialogue import *
from location_definitions import *
from girl_definitions import *
from elements import *

e = Engine()
i = Input()
d = Dialogue()
mc = Character()
e.build_locations(location_list)
e.build_girls(girl_list)

##### intro/setup game ######
e.introduction(introduction)
mc.get_name("jake")

#### begin game #####
e.activate_location('home_exterior', i, mc)
e.start_day()

while e.game_over != True:
    if str(e.state) == 'day_state':
        e.get_input(i, mc)
    elif str(e.state) == 'dialogue_state':
        d.get_dialogue(e, mc, e.girls['tammy'])