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
            
    
    def make_date(self, location, girl):
        location.is_date = True
        location.date_girl = girl
        
    def date(self, location, player):
        #describe location Experience
        print location.date_description
        time.sleep(0.5)

        #check if Girl has affinity for Location (increase experience chance)
        if location.name == location.date_girl.affinity:
            print location.date_girl.name, "loves it here!"
            exp_chance_increase = 3
        else:
            exp_chance_increase = 0

    ########################################################################
    #To Do: Check if Experience has already occured.
    #Nothing wrong with it occuring again, but if it has already occured
    #then there should be a slight difference in the experience, and
    #you won't get another EXP increase for doing it again.
    ########################################################################

        #roll to see if EXP happens (based on exp count, girl affinity and
        #location rarity of exp occurance)
        exp_chance = random.randint(1,location.experience_count - exp_chance_increase)

        #if EXP happens, you can commit to her and she can fall in love with
        #you on first "Hang"
        if exp_chance == 1:
            print "EXP OCCURRED!"
            player.experiences[location.experience_gained] = True

            if location.date_girl.committed_in != True:
                player.commit(location.date_girl)
            love_chance = random.randint(1,location.date_girl.love_count)
            if love_chance == 1:
                print "She fell in love with you."
                self.fall_in_love(player, location.date_girl)
            else:
                location.date_girl.love_count -= 1

        #if EXP does not happen, you can commit to her. Check if not first date
        #She can fall in love with you if not first date.
        else:
            if location.date_girl.committed_in != True:
                player.commit(location.date_girl)
            if location.date_girl.first_hangout == True:
                time.sleep(0.5)
                love_chance = random.randint(1,location.date_girl.love_count)
                if love_chance == 1:
                    print "She almost fell in love with you (but didn't cause it was your first time hanging out)."    
                location.date_girl.first_hangout = False
            else:
                love_chance = random.randint(1,location.date_girl.love_count)
                if love_chance == 1:
                    print "She fell in love with you."
                    self.fall_in_love(player, location.date_girl)
                else:
                    location.date_girl.love_count -= 1

        #subtract 1 from location experience count, every time visited
        #no matter what
        self.current_location.experience_count -= 1
        
        print "End of Date."
        location.is_date = False
        self.start_day()
        
    def fall_in_love(self, player, girl):
        endings.check_ending(player, girl)
        self.end_game = True
    
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
                        print "Sure! Where to?"
                        print 1, '-', "Let's go to the club."
                        print 2, '-', "Let's go for a nice hike."
                        print 3, '-', "Let's go out for dinner at that new restaurant."
                        print 4, '-', "Let's go to the theatre for a show."
                        
                        date_destination = raw_input("> ")
                        
                        print "Ok. That sounds good. I will see you there."
                        time.sleep(0.6)
                        
                        if int(date_destination) == 1:
                            engine.make_date(engine.locations['club'], character)
                        elif int(date_destination) == 2:
                            engine.make_date(engine.locations['river'], character)
                        elif int(date_destination) == 3:
                            engine.make_date(engine.locations['restaurant'], character)
                        elif int(date_destination) == 4:
                            engine.make_date(engine.locations['city'], character)
                         
                        #leave dialogue loop as soon as date initiated.
                        break   
                        
        #leave "Get Dialogue" back to "day loop"                
        engine.start_day()