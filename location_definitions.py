location_list = {
    "city":{
        'ident':01,
        'destinations':{
            'north':"mountains",
            'south':"home_exterior"
        },
        'description':"this is the description of the city",
        'date_description':"this is the DATE description of the city"
    },
    "home_exterior":{
        'ident':02,
        'destinations':{
            'north':"city",
            'south':"river",
            'inside': "home_interior"
        },
        'description':"description of home exterior",
        'date_description':"description of Date at home exterior"
    },
    "home_interior":{
        'ident':03,
        'destinations':{
            'outside': "home_exterior"
        },
        'description':"description of home interior",
        'date_description':"description of Date at home interior"
    }
}