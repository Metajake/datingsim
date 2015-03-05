import random

class Location(object):
    def __init__(self, name, destinations, description, date_description, verbs, nouns, inactive_verbs, observations, experience_gained):
        self.name = name
        self.destinations = destinations
        self.description = description
        self.date_description = date_description        
        self.verbs = verbs
        self.nouns = nouns
        self.inactive_verbs = inactive_verbs
        self.observations = observations
        self.characters = []
        self.experience_count = 15
        self.experience_gained = experience_gained
        self.is_date = False
        self.date_girl = None

    def describe(self):
        print self.description

    def describe_thing(self, thing):
        print self.nouns[thing]

def activate_location(engine, destination, inputobj, player):
    #if a 'current location already exists set new destination to current
    #location based off it's relationship to current location
    if engine.current_location:
        if destination in engine.current_location.destinations.keys():
            new_location = engine.current_location.destinations[destination]
            engine.current_location = engine.locations[new_location]
        else:
            engine.current_location = engine.locations[destination]
    else:
        engine.current_location = engine.locations[destination]
        
    #check if destination location is a date
    if engine.current_location.is_date == True:
        print "I'm excited to meet %s here for our date." % engine.current_location.date_girl.name
        engine.start_date()
    else:
        print "I am currently at the "+ str(engine.current_location.name) + "."
        #clear list of characters in location (for both INPUTOBJ and LOCATION obj)
        #repopulate list of avaiable characters based on current location
        del inputobj.character[:]
        del engine.current_location.characters[:]
        for k, v in engine.girls.iteritems():
            if v.meet_at != 'none':
                if engine.current_location.name == v.meet_at:
                    inputobj.character.append(k)
                    engine.current_location.characters.append(k)
                    print "%s is here." % k
                    v.meet_her_at()
            else:
                see_at = random.choice(v.see_at)
                if engine.current_location.name == see_at:
                    inputobj.character.append(k)
                    engine.current_location.characters.append(k)
                    print "%s is here." % k
                
    #add currect location to player.known_locations if its not already there
    if engine.current_location.name not in player.known_locations:            
        player.known_locations.append(engine.current_location.name)

    #clear the list of directions you can go    
    #repopulate list of available directions based on current location
    del inputobj.direction[:]
    for k, v in engine.current_location.destinations.iteritems():
        inputobj.direction.append(k)

    ###NOTE!!!!!!!!!!
    ###ADD DEFAULT VERBS!!!!!!!!!
    #AND add location verbs to inputobject verb list
    del inputobj.verb[:]
    inputobj.verb = ['go','give','leave','use','look', 'talk']
    for k, v in engine.current_location.verbs.iteritems():
        inputobj.verb.append(k)
        
    #add location nouns to inputobject verb list
    del inputobj.noun[:]
    for k, v in engine.current_location.nouns.iteritems():
        inputobj.noun.append(k)
        
    #add location inactive verbs to inputobjects inactive verb list
    del inputobj.inactive_verb[:]
    for k, v in engine.current_location.inactive_verbs.iteritems():
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
    inputobj.vocab['character'] = inputobj.character