import time, random
import endings
from locationobj import *

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
            obj = Location(key, value['destinations'], value['description'], value['date_description'], value['verbs'], value['nouns'], value['inactive_verbs'], value['observations'], value['experience_gained'])
            self.locations[key] = obj
            
    def build_girls(self, girl_list):
        for key, value in girl_list.iteritems():
            obj = Girl(key, value['love'], value['prude'], value['meet_at'], value['see_at'], value['affinity'], value['dialogue_tree'])
            self.girls[key] = obj
            
    #Engine Action Functions
    def make_date(self, location, girl):
        location.is_date = True
        location.date_girl = girl
                
    def fall_in_love(self, player, girl):
        endings.check_ending(player, girl)
        self.game_over = True
                                    
class Character(object):
    def __init__(self):
        self.name = ""
        self.known_locations = ['club', 'work']
        self.known_girls = []
        self.commits = 3
        self.committed_to = ""
        self.experiences = {
            "need_to_protect": False
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
    def __init__(self, name, love_count, prude, meet_at, see_at, affinity, dialogue_tree):
        self.name = name
        self.love_count = love_count
        self.prude = prude
        self.meet_at = meet_at
        self.see_at = see_at
        self.affinity = affinity
        self.dialogue_tree = dialogue_tree
        self.opinion = 0
        self.committed_in = False
        self.first_hangout = True
    
    def meet_her_at(self, destination="none"):
        self.meet_at = destination
        