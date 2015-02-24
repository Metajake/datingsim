location_list = {
    "city":{
        'ident':01,
        'destinations':{
            'north':"mountains",
            'south':"home_exterior"
        },
        'description':"this is the description of the city",
        'date_description':"this is the DATE description of the city",
        'verbs':{
            'think':'The size and scope of humanity is both fearsome and exciting. The city always reminds you of this feeling.'
        },
        'nouns':{
            'something':"it looks great"
        }
    },
    "home_exterior":{
        'ident':02,
        'destinations':{
            'north':"city",
            'south':"river",
            'inside': "home_interior"
        },
        'description':"description of home exterior",
        'date_description':"description of Date at home exterior",
        'verbs':{
            'think':'You miss your mom.'
        },
        'nouns':{
            'home':'Your landlord does a great job keeping your apartment looking nice.'
        }
    },
    "home_interior":{
        'ident':03,
        'destinations':{
            'outside': "home_exterior"
        },
        'description':"description of home interior",
        'date_description':"description of Date at home interior",
        'verbs':{
            'masturbate':'Busting a nut feels great but you don\'t get any life changing experience from it.'
        },
        'nouns':{
            'dog':'Your dog looks happy.'
        }
    }
}