from engine_text import *
from getinputobject import *
from getdialogue import *
from location_definitions import *
from girl_definitions import *
from elements import *
from expobject import *

e = Engine()
i = Input()
d = Dialogue()
exp = Experience()
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
        i.get_input(e, mc)
    elif str(e.state) == 'dialogue_state':
        #remove MC.Focus character as an argment and just reference it directly
        #off of MC inside the function
        d.get_dialogue(e, mc, mc.focus_character)
    elif str(e.state) == 'date_state':
        exp.date(e, mc)