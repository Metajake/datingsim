import time, random
import endings

#GAme States
class EngineDisabled(object):
    def __repr__(self):
        return "disabled_state"
        
    def idle_engine(self, engine):
        engine.state = EngineIdle()
        
    def enable_dialogue(self, engine):
        engine.state = DialogueEnabled()
    
    def enable_day(self, engine):
        engine.state = DayEnabled()
        
    def enable_date(self, engine):
        engine.state = DateEnabled()

class EngineIdle(EngineDisabled):
    def __repr__(self):
        return "idle_state"
        
class DialogueEnabled(EngineDisabled):
    def __repr__(self):
        return "dialogue_state"

    def disable_dialogue(self, engine):
        engine.state = EngineIdle()
        
class DayEnabled(EngineDisabled):
    def __repr__(self):
        return "day_state"

    def disable_day(self, engine):
        engine.state = EngineIdle()
        
class DateEnabled(EngineDisabled):
    def __repr__(self):
        return "date_state"
        
    def disable_date(self, engine):
        engine.state = EngineIdle()
    
#Game object
class Engine(object):
    def __init__(self):
        self.game_over = False
        self.current_location = None
        self.locations = {}
        self.girls = {}
        self.state = EngineDisabled()
        self.dates = []
        
    #State Functions
    def idle_engine(self):
        self.state.idle_engine(self)
    def start_dialogue(self):
        self.state.enable_dialogue(self)
    def start_day(self):
        self.state.enable_day(self)
        self.current_location.describe()
    def start_date(self):
        self.state.enable_date(self)
        self.current_location.describe()
        
    #Engine Setup functions
    def introduction(self, text):
        time.sleep(0.5)
        print text
        
    def build_locations(self, location_list):
        for key, value in location_list.iteritems():
            obj = Location(key, value['destinations'], value['description'], value['date_description'], value['verbs'], value['nouns'], value['inactive_verbs'], value['observations'], value['experience_count'], value['experience_gained'])
            self.locations[key] = obj
            
    def build_girls(self, girl_list):
        for key, value in girl_list.iteritems():
            obj = Girl(key, value['love'], value['prude'], value['location'], value['opinion'], value['affinity'], value['dialogue_tree'])
            self.girls[key] = obj
            
    #Engine Action Functions
    def make_date(self, location, girl):
        location.is_date = True
        location.date_girl = girl
                
    def fall_in_love(self, player, girl):
        endings.check_ending(player, girl)
        self.game_over = True
    
    def activate_location(self, destination, inputobj, player):
        if self.current_location:
            if destination in self.current_location.destinations.keys():
                new_location = self.current_location.destinations[destination]
                self.current_location = self.locations[new_location]
            else:
                self.current_location = self.locations[destination]
        else:
            self.current_location = self.locations[destination]
            
        if self.current_location.is_date == True:
            print "I'm excited to meet her here for our date."
            self.start_date()
        else:
            print "I am currently at the "+ str(self.current_location.name)+"."
                    
        player.known_locations.append(self.current_location.name)

        #clear the list of directions you can go    
        #repopulate list of available directions based on current location
        del inputobj.direction[:]
        for k, v in self.current_location.destinations.iteritems():
            inputobj.direction.append(k)

        #add location verbs to inputobject verb list
        del inputobj.verb[:]
        inputobj.verb = ['go','give','leave','use','look', 'talk']
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
        
        ####### PUTTING THIS HERE. NOT SURE IF GOES ELSEWHERE BETTER!!! ########
        #appends list of player known locations to get_input "destinations"
        for i in player.known_locations:
            inputobj.direction.append(i)
        
        #update Input Object's "Vocab" lists
        inputobj.vocab['verb'] = inputobj.verb
        inputobj.vocab['direction'] = inputobj.direction
        inputobj.vocab['noun'] = inputobj.noun
        inputobj.vocab['inactive_verb'] = inputobj.inactive_verb
                                
class Location(object):
    def __init__(self, name, destinations, description, date_description, verbs, nouns, inactive_verbs, observations, experience_count, experience_gained):
        self.name = name
        self.destinations = destinations
        self.description = description
        self.date_description = date_description        
        self.verbs = verbs
        self.nouns = nouns
        self.inactive_verbs = inactive_verbs
        self.observations = observations
        self.experience_count = experience_count
        self.experience_gained = experience_gained
        self.is_date = False
        self.date_girl = None

    def describe(self):
        print self.description

    def describe_thing(self, thing):
        print self.nouns[thing]

class Character(object):
    def __init__(self):
        self.name = ""
        self.known_locations = ['club']
        self.known_girls = []
        self.commits = 3
        self.committed_to = ""
        self.experiences = {
            "need_to_protect": True
        }
        focus_character = None
        
    def focus(self, character=None):
        if character:
            self.focus_character = character
        else:
            self.focus_character = None

    def get_name(self, name=""):
        if name:
            self.name = name
        else:
            print "What is your name?"
            self.name = raw_input("> ")
    
    def make_acquaintance(self, girl):
        self.known_girls.append(girl.name)
        #return "My name is %s." % self.name
        
    def reflect(self):
        print "My name is", self.name
        print "My known locations are: "+str(self.known_locations)
        
    def commit(self, girl):
        print "Would you like to commit to her?"
        if self.commits > 0:
            commit = raw_input("> ")
            if commit == "yes":
                self.committed_to = girl.name
                print "I'm committed to", self.committed_to
                girl.committed_in = True
                self.commits -= 1
        else:
            print "No more commits left."

class Girl(object):
    def __init__(self, name, love_count, prude, prefer_location, opinion, affinity, dialogue_tree):
        self.name = name
        self.love_count = love_count
        self.prude = prude
        self.prefer_location = prefer_location
        self.opinion = opinion
        self.affinity = affinity
        self.dialogue_tree = dialogue_tree
        self.committed_in = False
        self.first_hangout = True