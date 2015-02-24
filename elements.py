class Character(object):
    def __init__(self, name):
        self.name = name
        self.known_locations = []
        
    def reflect(self):
        print "My known locations are: "+str(self.known_locations)
    
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
    def __init__(self, name, destinations, description, date_description, verbs):
        self.name = name
        self.destinations = destinations
        self.description = description
        self.date_description = date_description        
        self.verbs = verbs
        
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
        
    def introduction(self):
        print "Welcome to ."
        
    def build_locations(self, location_list):
        for key, value in location_list.iteritems():
            obj = Location(key, value['destinations'], value['description'], value['date_description'], value['verbs'])
            self.locations[key] = obj
            
    def build_girls(self, girl_list):
        for key, value in girl_list.iteritems():
            obj = Girl(key, value['love'], value['prude'], value['location'])
            self.girls[key] = obj
            
    def activate_location(self, destination, inputobj, character):
        if self.current_location:
            print "my current location is", self.current_location.name
            new_location = self.current_location.destinations[destination]
            self.current_location = self.locations[new_location]
        else:
            self.current_location = self.locations[destination]
            
        print "I am currently at the "+ str(self.current_location.name)+"."
        self.current_location.describe()
        
        character.known_locations.append(self.current_location.name)

        #clear the list of directions you can go    
        #repopulate list of available directions based on current location
        del inputobj.direction[:]
        for k, v in self.current_location.destinations.iteritems():
            inputobj.direction.append(k)

        #add location sensitive verbs to inputobject verb list
        del inputobj.verb[:]
        inputobj.verb = ['go','give','leave','use','look']
        for k, v in self.current_location.verbs.iteritems():
            inputobj.verb.append(k)
        
        #update Input Object's "Vocab" lists
        inputobj.vocab['verb'] = inputobj.verb
        inputobj.vocab['direction'] = inputobj.direction
        
    def get_input(self, inputobj, character):
        s = inputobj.scan(raw_input("> "), inputobj)
        x = inputobj.parse_sentence(s)
        #print x
        if x.verb.lower() == 'go':
            self.activate_location(x.object.lower(), inputobj, character)
        elif x.verb.lower() == "reflect":
            character.reflect()
        elif x.verb.lower() == "look":
            if x.object == "none":
                self.current_location.describe()
            else:
                x.object.describe()