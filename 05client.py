#-
from engine_text import *
from getinputobject import *
from getdialogue import *
from location_definitions import *
from girl_definitions import *
from elements import *
from expobject import *
from locationobj import *
from graphicsobj import *

e = Engine()
i = Input()
d = Dialogue()
exp = Experience()
mc = Character()
g = Graphics()

e.build_locations(location_list)
e.build_girls(girl_list)

##### intro/setup game ######
g.initialize()
e.introduction(introduction)
mc.get_name("jake")

#### begin game #####
activate_location(e,'residential district', i, mc)
e.start_day()

while e.game_over != True:
    if str(e.state) == 'day_state':
        i.get_input(e, mc)
    elif str(e.state) == 'dialogue_state':
        d.get_dialogue(e, mc)
    elif str(e.state) == 'date_state':
        exp.date(e, mc)