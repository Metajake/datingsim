from getinputobject import *
from location_definitions import *
from girl_definitions import *
    
class Event(object):
    """an object to trigger scripted character appearences, dialogue, encounters, movement, etc."""
    def __init__(self):
        pass
        
class Scene(object):
    """an object to indicate who and what is in our current location."""
    def __init__(self, location, girl):
        self.location = location
        self.girl = girl

class Location(object):
    def __init__(self, name, destinations, description, date_description):
        self.name = name
        self.destinations = destinations
        self.description = description
        self.date_description = date_description        
        
    def describe(self):
        print self.description
        
class Girl(object):
    def __init__(self, name, fall_in_love, prude, prefer_location):
        self.name = name
        self.fall_in_love = fall_in_love
        self.prude = prude
        self.prefer_location = prefer_location
    
class Engine(object):
    def __init__(self):
        self.game_over = False
        self.current_location = None
        self.locations = {}
        self.girls = {}
        
    def build_locations(self):
        for key, value in location_list.iteritems():
            obj = Location(key, value['destinations'], value['description'], value['date_description'])
            self.locations[key] = obj
            
    def build_girls(self):
        for key, value in girl_list.iteritems():
            obj = Girl(key, value['love'], value['prude'], value['location'])
            self.girls[key] = obj
            
    def activate_location(self, destination, inputobj):
        print "Activating Location"
        
        if self.current_location:
            print "my current location is", self.current_location.name
            new_location = self.current_location.destinations[destination]
            print new_location
            self.current_location = self.locations[new_location]
            self.current_location.describe()
        else:
            self.current_location = self.locations[destination]
            self.current_location.describe()
        
        #clear the list of directions you can go    
        del inputobj.direction[:]
        #repopulate the list of available directions based on current location
        for k, v in self.current_location.destinations.iteritems():
            inputobj.direction.append(k)
                
    def get_input(self, inputobj):
        s = inputobj.scan(raw_input("> "))
        x = inputobj.parse_sentence(s)
        if x.verb.lower() == 'go':
            self.activate_location(x.object.lower(), inputobj)

e = Engine()
i = Input()
e.build_locations()
e.build_girls()

e.activate_location('home_exterior', i)

while e.game_over != True:
    #print i.direction
    e.get_input(i)