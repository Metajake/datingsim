import time

class Event(object):
    """an object to trigger scripted character appearances, dialogue, encounters, movement, etc."""
    def __init__(self):
        pass
        
class Scene(object):
    """an object to indicate who and what is in our current location."""
    def __init__(self, location, characters=[]):
        self.location = location
        if characters:
            self.characters = characters

class Location(object):
    def __init__(self, name, destinations, description, date_description, verbs, nouns, inactive_verbs):
        self.name = name
        self.destinations = destinations
        self.description = description
        self.date_description = date_description        
        self.verbs = verbs
        self.nouns = nouns
        self.inactive_verbs = inactive_verbs
        
    def describe(self):
        print self.description
        
    def describe_thing(self, thing):
        print self.nouns[thing]
        
class Character(object):
    def __init__(self):
        self.name = ""
        self.known_locations = []
    
    def get_name(self, name=""):
        print "What is your name?"
        if name:
            self.name = "Kosek"
        else:
            self.name = raw_input("> ")

    def reflect(self):
        print "My name is", self.name
        print "My known locations are: "+str(self.known_locations)

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
        time.sleep(0.5)
        print """Welcome to the the pre-Alpha of a dating sim tentatively titled 'Don\'t Let Her Fall in Love with You'.

        You are a game development educator and part time student. Your goal is to achieve a number of life-enhancing experiences through shared time with women. By spending time with them, inevitably, every woman will eventually fall in love with you. In return, unless you are committed to one, you risk falling in love with them, before they leave you only to have your heart shattered. The number of life enhancing experiences you have determines the strength of your commitment and ultimately the outcome of your connection with your one... true... love.

        Try pressing ? at any time."""
        
    def build_locations(self, location_list):
        for key, value in location_list.iteritems():
            obj = Location(key, value['destinations'], value['description'], value['date_description'], value['verbs'], value['nouns'], value['inactive_verbs'])
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

        #add location verbs to inputobject verb list
        del inputobj.verb[:]
        inputobj.verb = ['go','give','leave','use','look']
        for k, v in self.current_location.verbs.iteritems():
            inputobj.verb.append(k)
            
        #add location nouns to inputobject verb list
        del inputobj.noun[:]
        for k, v in self.current_location.nouns.iteritems():
            inputobj.noun.append(k)
            
        #add location inactive verbs to inputobjects inactive verb list
        del inputobj.inactive_verb[:]
        for k, v in self.current_location.inactive_verbs.iteritems():
            inputobj.inactive_verb.append(k)
        
        #update Input Object's "Vocab" lists
        inputobj.vocab['verb'] = inputobj.verb
        inputobj.vocab['direction'] = inputobj.direction
        inputobj.vocab['noun'] = inputobj.noun
        inputobj.vocab['inactive_verb'] = inputobj.inactive_verb
        
    def get_input(self, inputobj, character):
        s = inputobj.scan(raw_input("> "), inputobj)
        #print s
        
        x = inputobj.parse_sentence(s)
        #for i in dir(x):
        #    print i
        #print x.subject
        
        if x.subject == 'error':
            inputobj.error_msg()
        
        if x.subject == 'inactive_player':
            print self.current_location.inactive_verbs[x.verb]
        
        if x.verb == "?":
            inputobj.help()
        if x.verb.lower() == 'go':
            if x.object.lower() == 'error':
                inputobj.error_msg()
            else:
                #Warning???? this MIGHT "erase" the list results of 's' above.
                self.activate_location(x.object.lower(), inputobj, character)
        elif x.verb.lower() == "reflect":
            character.reflect()
        elif x.verb.lower() == "look":
            if x.object == "none":
                self.current_location.describe()
            else:
                self.current_location.describe_thing(x.object)