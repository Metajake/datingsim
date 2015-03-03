import random, time

class Dialogue(object):
    def __init__(self):
        self.levels = 5
                
    def get_dialogue(self, engine, player):
        print """
        %s stands in front of you.
        """ % player.focus_character.name
        
        print "Hello..."
        
        for i in range(self.levels):

            print "dialogue level", i
            print "character opionion", player.focus_character.opinion

            print "(Enter your choice)"

            if player.focus_character.name not in player.known_girls:
                print 1, '-', player.focus_character.dialogue_tree[i]['statement']['compliment']
                print 2, '-', player.focus_character.dialogue_tree[i]['statement']['introduction'], player.name
                print 3, '-', player.focus_character.dialogue_tree[i]['statement']['question']
                
                statement = raw_input("> ")
                #print statement
                
                if int(statement) == 1:
                    print player.focus_character.dialogue_tree[i]['reply']['compliment'][0]
                    player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['compliment'][1]
                elif int(statement) == 2:
                    player.make_acquaintance(player.focus_character)
                    print player.focus_character.dialogue_tree[i]['reply']['introduction'][0]
                    player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['introduction'][1]
                elif int(statement) == 3:
                    print player.focus_character.dialogue_tree[i]['reply']['question'][0]
                    player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['question'][1]
            else:
                if player.focus_character.opinion < 3:
                    print 1, '-', player.focus_character.dialogue_tree[i]['statement']['compliment']
                    print 2, '-', random.choice(engine.current_location.observations)
                    print 3, '-', player.focus_character.dialogue_tree[i]['statement']['question']
                
                    statement = raw_input("> ")
                
                    if int(statement) == 1:
                        print player.focus_character.dialogue_tree[i]['reply']['compliment'][0]
                        player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['compliment'][1]
                    elif int(statement) == 2:
                        print player.focus_character.dialogue_tree[i]['reply']['observation'][0]
                        player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['observation'][1]
                    elif int(statement) == 3:
                        print player.focus_character.dialogue_tree[i]['reply']['question'][0] 
                        player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['question'][1]            
                else:
                    print 1, '-', player.focus_character.dialogue_tree[i]['statement']['compliment']
                    print 2, '-', random.choice(engine.current_location.observations)
                    print 3, '-', player.focus_character.dialogue_tree[i]['statement']['question']
                    print 4, '-', "Would you like to go on a date?"
                
                    statement = raw_input("> ")
                
                    if int(statement) == 1:
                        print player.focus_character.dialogue_tree[i]['reply']['compliment'][0]
                        player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['compliment'][1]
                    elif int(statement) == 2:
                        print player.focus_character.dialogue_tree[i]['reply']['observation'][0]
                        player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['observation'][1]
                    elif int(statement) == 3:
                        print player.focus_character.dialogue_tree[i]['reply']['question'][0]               
                        player.focus_character.opinion += player.focus_character.dialogue_tree[i]['reply']['question'][1]
                    elif int(statement) == 4:
                        print "Sure! Where to?"
                        print 1, '-', "Let's go to the club."
                        print 2, '-', "Let's go for a nice hike."
                        print 3, '-', "Let's go out for dinner at that new restaurant."
                        print 4, '-', "Let's go to the theatre for a show."
                        
                        date_destination = raw_input("> ")
                        
                        print "Ok. That sounds good. I will see you there."
                        time.sleep(0.3)
                        
                        if int(date_destination) == 1:
                            engine.make_date(engine.locations['club'], player.focus_character)
                        elif int(date_destination) == 2:
                            engine.make_date(engine.locations['river'], player.focus_character)
                        elif int(date_destination) == 3:
                            engine.make_date(engine.locations['restaurant'], player.focus_character)
                        elif int(date_destination) == 4:
                            engine.make_date(engine.locations['city'], player.focus_character)
                         
                        #leave dialogue loop as soon as date initiated.
                        break   
                        
        #leave "Get Dialogue" back to "day loop"                
        engine.start_day()