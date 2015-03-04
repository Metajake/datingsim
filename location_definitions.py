location_list = {
    "city":{
        'destinations':{
            'north':"historic district",
            'south':"residential district",
            'east':'night life district',
            'west':'theatre district',
            'gym':'gym',
            'work':'work'
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
    "theatre district":{
        'destinations':{
            'east':'city',
            'theatre':'theatre'
        },
        'description':"this is the description of the theatre district",
        'date_description':"this is the DATE description of the theatre district",
        'verbs':{},
        'nouns':{
            'something':"it looks great"
        },
        'inactive_verbs':{},
        'observations':['It sure is nice out today.'],
        'experience_gained':None
    },
    "theatre":{
        'destinations':{
            'outside':'theatre district'
        },
        'description':"this is the description of the theatre",
        'date_description':"this is the DATE description of the theatre",
        'verbs':{},
        'nouns':{
            'something':"it looks great"
        },
        'inactive_verbs':{},
        'observations':['It sure is nice here today.'],
        'experience_gained':None
    },
    "residential district":{
        'destinations':{
            'north':"city",
            'south':"river",
            'inside': "home",
            'west':'shopping district',
            'east':'walking path'
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
        'experience_gained':"provide for"
    },
    "gym":{
        'destinations':{
            'outside': "city"
        },
        'description':"description of gym",
        'date_description':"The gym is bumping.",
        'verbs':{},
        'nouns':{
            'people':'They are hot and sweaty, moving to the beat of the treadmill.'
        },
        'inactive_verbs':{
            'dance':'working it!'
        },
        'observations':['This workout is great.'],
        'experience_gained':None
    },
    "club":{
        'destinations':{
            'outside': "night life district"
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
        'experience_gained':"need to protect"
    },
    "work":{
        'destinations':{
            'outside': "city"
        },
        'description':"description of work",
        'date_description':"The work is bustling.",
        'verbs':{},
        'nouns':{},
        'inactive_verbs':{
            'work':'I\'m devving so hard!'
        },
        'observations':['This work is great.'],
        'experience_gained':None
    },
    "bar":{
        'destinations':{
            'outside': "night life district"
        },
        'description':"description of bar",
        'date_description':"Drink.",
        'verbs':{},
        'nouns':{},
        'inactive_verbs':{
            'drink':'I\'m drunk..'
        },
        'observations':['drinking sure is awesome.'],
        'experience_gained':None
    },
    "night life district":{
        'destinations':{
            'west': "city",
            'club':'club',
            'bar':'bar'
        },
        'description':"description of night life disctrict.",
        'date_description':"This part of town is wild. She seems into it.",
        'verbs':{},
        'nouns':{},
        'inactive_verbs':{},
        'observations':['The women are hot. The guys are tools.'],
        'experience_gained':None
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
            'restaurant':'restaurant',
            'store':'store'
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
    },
    "store":{
        'destinations':{
            'outside':"shopping district"
        },
        'description':"this is the description of the shop.",
        'date_description':"this is the DATE description of the shop",
        'verbs':{},
        'nouns':{},
        'inactive_verbs':{
            'hike':'buying stuff!',
        },
        'observations':['There\'s a lot to buy.'],
        'experience_gained':None
    },
    "historic district":{
        'destinations':{
            'south':"city",
            'east':'gallery'
        },
        'description':"this is the description of the historic residential district. To the north, the steep, beautiful mountains protect the neighborhoods.",
        'date_description':"this is the DATE description of the historic residential district",
        'verbs':{
            'think':'Beautiful...'
        },
        'nouns':{
            'buildings':"old homefronts look great."
        },
        'inactive_verbs':{},
        'observations':['It sure is nice in the historic district today.'],
        'experience_gained':None
    },
    "her place":{
        'destinations':{
            'outside':"historic district"
        },
        'description':"this is the description of her place.",
        'date_description':"this is the DATE description of her place",
        'verbs':{
            'relax':'Commercialism...'
        },
        'nouns':{
            'people':"capitolism is sweet."
        },
        'inactive_verbs':{},
        'observations':['It sure is nice in the shopping district today.'],
        'experience_gained':'cared for'
    },
    "gallery":{
        'destinations':{
            'west':"historic district"
        },
        'description':"this is the description of the gallery.",
        'date_description':"this is the DATE description of the gallery",
        'verbs':{
            'observe':'the art is nice...',
            'critique': "this piece represents more then necessary."
        },
        'nouns':{
            'art':"It's great that this artist put in so much effort."
        },
        'inactive_verbs':{},
        'observations':['The art is nice.'],
        'experience_gained':None
    },
    "walking path":{
        'destinations':{
            'west':"residential district",
            'east':'school'
        },
        'description':"this is the description of the walking path.",
        'date_description':"this is the DATE description of the walking path",
        'verbs':{},
        'nouns':{
            'trees':"The surroundings are nice."
        },
        'inactive_verbs':{
            'run':'getting my heart rate up feels good.'
        },
        'observations':['These paths are nice.'],
        'experience_gained':None
    },
    "school":{
        'destinations':{
            'west':"walking path"
        },
        'description':"this is the description of the school.",
        'date_description':"this is the DATE description of the school",
        'verbs':{},
        'nouns':{
            'classrooms':"I have learned a lot here.",
            'students': "the peeps are learning"
        },
        'inactive_verbs':{
            'study':'learningz!',
            'research': "Researchannn"
        },
        'observations':['There\'s a lot to learn.'],
        'experience_gained':None
    },
    "river":{
        'destinations':{
            'north':"residential district",
            'south':'hiking trails'
        },
        'description':"this is the description of the river.",
        'date_description':"this is the DATE description of the river",
        'verbs':{},
        'nouns':{},
        'inactive_verbs':{
            'canoe':'canoeing!',
        },
        'observations':['There\'s a lot to canoe.'],
        'experience_gained':None
    },
    "hiking trails":{
        'destinations':{
            'north':"river"
        },
        'description':"this is the description of the hills.",
        'date_description':"this is the DATE description of the river",
        'verbs':{},
        'nouns':{},
        'inactive_verbs':{
            'hike':'beautiful hike!',
        },
        'observations':['There\'s a lot to hike.'],
        'experience_gained':None
    }
}