location_list = {
    "city":{
        'destinations':{
            'north':"mountains",
            'south':"residential district",
            'east':'night life district'
        },
        'description':"this is the description of the city",
        'date_description':"this is the DATE description of the city",
        'verbs':{
            'think':'The size and scope of humanity is both fearsome and exciting. The city always reminds you of this feeling.'
        },
        'nouns':{
            'something':"it looks great"
        },
        'inactive_verbs':{},
        'observations':['It sure is nice out today.'],
        'experience_gained':None
    },
    "residential district":{
        'destinations':{
            'north':"city",
            'south':"river",
            'inside': "home",
            'west':'shopping district'
        },
        'description':"description of residential district",
        'date_description':"description of Date at residential district",
        'verbs':{
            'think':'You miss your mom.'
        },
        'nouns':{
            'home':'Your landlord does a great job keeping your apartment looking nice.'
        },
        'inactive_verbs':{},
        'observations':['It sure is nice outside of my home today.'],
        'experience_gained':None
    },
    "home":{
        'destinations':{
            'outside': "residential district"
        },
        'description':"description of home",
        'date_description':"description of Date at home",
        'verbs':{},
        'nouns':{
            'dog':'Your dog looks happy.'
        },
        'inactive_verbs':{
            'masturbate':'Busting a nut feels great but you don\'t get any life changing experience from it.'
        },
        'observations':['It sure is nice in here today.'],
        'experience_gained':"provide_for"
    },
    "club":{
        'destinations':{
            'outside': "city"
        },
        'description':"description of club",
        'date_description':"The club is bumping.",
        'verbs':{},
        'nouns':{
            'people':'They are hot and sweaty, moving to the beat of the music.'
        },
        'inactive_verbs':{
            'dance':'Shaking it!'
        },
        'observations':['This music is great.'],
        'experience_gained':"need_to_protect"
    },
    "work":{
        'destinations':{
            'outside': "city"
        },
        'description':"description of work",
        'date_description':"Working late can be exhilerating.",
        'verbs':{},
        'nouns':{
            'people':'They are hot and sweaty, moving to the beat of the music.'
        },
        'inactive_verbs':{
            'work':'I\m dev-ing so hard!!'
        },
        'observations':['Work sure is awesome.'],
        'experience_gained':"make_another_jealous"
    },
    "restaurant":{
        'destinations':{
            'outside':"shopping district"
        },
        'description':"this is the description of the restaurant",
        'date_description':"the candle light sets the mood perfectly. The wine makes you feel so good.",
        'verbs':{
            'eat':'Yum. Careful not to fill up too much.'
        },
        'nouns':{
            'something':"it looks great"
        },
        'inactive_verbs':{},
        'observations':['I hear that they have the best food in town.'],
        'experience_gained':"need to provide"
    },
    "shopping district":{
        'destinations':{
            'east':"residential district",
            'restaurant':'restaurant'
        },
        'description':"this is the description of the shopping district",
        'date_description':"this is the DATE description of the shopping district",
        'verbs':{
            'think':'Commercialism...'
        },
        'nouns':{
            'people':"capitolism is sweet."
        },
        'inactive_verbs':{},
        'observations':['It sure is nice in the shopping district today.'],
        'experience_gained':None
    }
}