import time, random

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
    
#Game object
class Engine(object):
    def __init__(self):
        self.game_over = False
        self.current_location = None
        self.locations = {}
        self.girls = {}
        self.state = EngineDisabled()
    
    #State Functions
    def idle_engine(self):
        self.state.idle_engine(self)
    def start_dialogue(self):
        self.state.enable_dialogue(self)
    def start_day(self):
        self.state.enable_day(self)
        self.current_location.describe()
        
    def introduction(self, text):
        time.sleep(0.5)
        print text
        
    def build_locations(self, location_list):
        for key, value in location_list.iteritems():
            obj = Location(key, value['destinations'], value['description'], value['date_description'], value['verbs'], value['nouns'], value['inactive_verbs'], value['observations'])
            self.locations[key] = obj
            
    def build_girls(self, girl_list):
        for key, value in girl_list.iteritems():
            obj = Girl(key, value['love'], value['prude'], value['location'], value['opinion'], value['dialogue_tree'])
            self.girls[key] = obj
            
    def activate_location(self, destination, inputobj, character):
        if self.current_location:
            print "my current location is", self.current_location.name
            new_location = self.current_location.destinations[destination]
            self.current_location = self.locations[new_location]
        else:
            self.current_location = self.locations[destination]
            
        print "I am currently at the "+ str(self.current_location.name)+"."
        #moved to self.start_day() .. will it work?
        #self.current_location.describe()
        
        character.known_locations.append(self.current_location.name)

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
        
        #update Input Object's "Vocab" lists
        inputobj.vocab['verb'] = inputobj.verb
        inputobj.vocab['direction'] = inputobj.direction
        inputobj.vocab['noun'] = inputobj.noun
        inputobj.vocab['inactive_verb'] = inputobj.inactive_verb
        
    #maybe come back and use this
    #def check_state(self, inputobj, character):
    #    #print self.state
    #    if str(self.state) == 'day_state':
    #        self.get_input(inputobj, character)
    #    elif self.state == 'dialogue_state':
    #        self.get_dialogue(inputobj, character)

        
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
                self.activate_location(x.object.lower(), inputobj, character)
        
        if x.verb.lower() == "talk":
            self.start_dialogue()
            
        if x.verb.lower() == "reflect":
            character.reflect()
        
        if x.verb.lower() == "look":
            if x.object == "none":
                self.current_location.describe()
            else:
                self.current_location.describe_thing(x.object)
                        
class Location(object):
    def __init__(self, name, destinations, description, date_description, verbs, nouns, inactive_verbs, observations):
        self.name = name
        self.destinations = destinations
        self.description = description
        self.date_description = date_description        
        self.verbs = verbs
        self.nouns = nouns
        self.inactive_verbs = inactive_verbs
        self.observations = observations

    def describe(self):
        print self.description

    def describe_thing(self, thing):
        print self.nouns[thing]

class Character(object):
    def __init__(self):
        self.name = ""
        self.known_locations = []
        self.known_girls = []

    def get_name(self, name=""):
        if name:
            self.name = "Kosek"
        else:
            print "What is your name?"
            self.name = raw_input("> ")
    
    def make_acquaintance(self, girl):
        self.known_girls.append(girl.name)
        #return "My name is %s." % self.name
        
    def reflect(self):
        print "My name is", self.name
        print "My known locations are: "+str(self.known_locations)

class Girl(object):
    def __init__(self, name, fall_in_love, prude, prefer_location, opinion, dialogue_tree):
        self.name = name
        self.fall_in_love = fall_in_love
        self.prude = prude
        self.prefer_location = prefer_location
        self.opinion = opinion
        self.dialogue_tree = dialogue_tree
                
class Dialogue(object):
    def __init__(self):
        self.levels = 5
                
    def get_dialogue(self, engine, player, character):
        print """
        %s stands in front of you.
        """ % character.name
        
        print "Hello..."
        
        for i in range(self.levels):

            print "dialogue level", i
            print "character opionion", character.opinion

            print "(Enter your choice)"

            if character.name not in player.known_girls:
                print 1, '-', character.dialogue_tree[i]['statement']['compliment']
                print 2, '-', character.dialogue_tree[i]['statement']['introduction'], player.name
                print 3, '-', character.dialogue_tree[i]['statement']['question']
                
                statement = raw_input("> ")
                #print statement
                
                if int(statement) == 1:
                    print character.dialogue_tree[i]['reply']['compliment'][0]
                    character.opinion += character.dialogue_tree[i]['reply']['compliment'][1]
                elif int(statement) == 2:
                    player.make_acquaintance(character)
                    print character.dialogue_tree[i]['reply']['introduction'][0]
                    character.opinion += character.dialogue_tree[i]['reply']['introduction'][1]
                elif int(statement) == 3:
                    print character.dialogue_tree[i]['reply']['question'][0]
                    character.opinion += character.dialogue_tree[i]['reply']['question'][1]
            else:
                if character.opinion < 3:
                    print 1, '-', character.dialogue_tree[i]['statement']['compliment']
                    print 2, '-', random.choice(engine.current_location.observations)
                    print 3, '-', character.dialogue_tree[i]['statement']['question']
                
                    statement = raw_input("> ")
                
                    if int(statement) == 1:
                        print character.dialogue_tree[i]['reply']['compliment'][0]
                        character.opinion += character.dialogue_tree[i]['reply']['compliment'][1]
                    elif int(statement) == 2:
                        print character.dialogue_tree[i]['reply']['observation'][0]
                        character.opinion += character.dialogue_tree[i]['reply']['observation'][1]
                    elif int(statement) == 3:
                        print character.dialogue_tree[i]['reply']['question'][0] 
                        character.opinion += character.dialogue_tree[i]['reply']['question'][1]            
                else:
                    print 1, '-', character.dialogue_tree[i]['statement']['compliment']
                    print 2, '-', random.choice(engine.current_location.observations)
                    print 3, '-', character.dialogue_tree[i]['statement']['question']
                    print 4, '-', "Would you like to go on a date?"
                
                    statement = raw_input("> ")
                
                    if int(statement) == 1:
                        print character.dialogue_tree[i]['reply']['compliment'][0]
                        character.opinion += character.dialogue_tree[i]['reply']['compliment'][1]
                    elif int(statement) == 2:
                        print character.dialogue_tree[i]['reply']['observation'][0]
                        character.opinion += character.dialogue_tree[i]['reply']['observation'][1]
                    elif int(statement) == 3:
                        print character.dialogue_tree[i]['reply']['question'][0]               
                        character.opinion += character.dialogue_tree[i]['reply']['question'][1]
                    elif int(statement) == 4:
                        print "Sure! :) "
                        
        engine.start_day()