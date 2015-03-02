import time, random

class Experience(object):
    def __init__(self):
        pass
        
    def date(self, engine, player):
        #describe location Experience
        print engine.current_location.date_description
        time.sleep(0.3)

        #check if Girl has affinity for Location (increase experience chance)
        if engine.current_location.name == engine.current_location.date_girl.affinity:
            print engine.current_location.date_girl.name, "loves it here!"
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
        #location rarity of exp occurance). If exp count too low, don't discount affinity
        if engine.current_location.experience_count < 5:
            exp_chance = random.randint(1,engine.current_location.experience_count)
        else:
            exp_chance = random.randint(1,engine.current_location.experience_count - exp_chance_increase)

        #if EXP happens, you can commit to her and she can fall in love with
        #you on first "Hang"
        if exp_chance == 1:
            print "EXP OCCURRED!"
            player.experiences[engine.current_location.experience_gained] = True

            if engine.current_location.date_girl.committed_in != True:
                player.commit(engine.current_location.date_girl)
            love_chance = random.randint(1,engine.current_location.date_girl.love_count)
            if love_chance == 1:
                print "She fell in love with you."
                engine.fall_in_love(player, engine.current_location.date_girl)
            else:
                engine.current_location.date_girl.love_count -= 1

        #if EXP does not happen, you can commit to her. Check if not first date
        #She can fall in love with you if not first date.
        else:
            if engine.current_location.date_girl.committed_in != True:
                player.commit(engine.current_location.date_girl)
            if engine.current_location.date_girl.first_hangout == True:
                time.sleep(0.5)
                love_chance = random.randint(1,engine.current_location.date_girl.love_count)
                if love_chance == 1:
                    print "She almost fell in love with you (but didn't cause it was your first time hanging out)."    
                engine.current_location.date_girl.first_hangout = False
            else:
                love_chance = random.randint(1,engine.current_location.date_girl.love_count)
                if love_chance == 1:
                    print "She fell in love with you."
                    engine.fall_in_love(player, engine.current_location.date_girl)
                else:
                    engine.current_location.date_girl.love_count -= 1

        #subtract 1 from location experience count, every time visited
        #no matter what (cant go below 2)
        if engine.current_location.experience_count > 2:
            engine.current_location.experience_count -= 1
        
        
        print "End of Date."
        engine.current_location.is_date = False
        engine.start_day()
    