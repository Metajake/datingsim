def check_ending(character, girl):
    if len(character.experiences) == 0:
        if girl.committed_in == True:
            print "She has fallen in love with you, and you are committed to her. Despite your inexperienced nature, the shared love and commitment will lead to new horizons, eternal respect, and unity."
        else:
            print "She has fallen in love with you. In turn you have fallen in love with her. Unfortunately, you lack commitment. Eventually she will leave you and you will be left heartbroken and shattered.\nGame over."
    elif len(character.experiences) > 0 and len(character.experiences) < 3:
        if girl.committed_in == True:
            print "barely experienced. Committed. ending 2"
        else:
            print "barely experienced. Uncommitted. game over 2"
    elif len(character.experiences) >= 3 and len(character.experiences) < 5:
        if girl.committed_in == True:
            print "somewhat experienced. Committed. ending 2"
        else:
            print "somewhat experienced. Uncommitted. game over 2"
    elif len(character.experiences) >= 5 and len(character.experiences) < 7:
        if girl.committed_in == True:
            print "very experienced. Committed. ending 2"
        else:
            print "very experienced. Uncommitted. game over 2"
    elif len(character.experiences) == 7:
        if girl.committed_in == True:
            print "completely experienced. Committed. ending 2"
        else:
            print "completely experienced. Uncommitted. game over 2"