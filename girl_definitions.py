girl_list = {
    "tammy":{
        "love":15,
        "prude":"easy",
        "location":"club",
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            0:{
                'statement':{
                    'compliment':"Your work from last week was really good.",
                    'introduction': 'Hi, my name is ',
                    'question': 'Do you know where I can have some copies of this document made?'
                },
                'reply':{
                    'compliment':["Thank you. Thats really nice of you to say.",1],
                    'introduction': ["Um.. That's nice.",0],
                    'question': ["I'm too busy.",-1],
                    'observation':['Yeah....', 0]
                }
            },
            1:{
                'statement':{
                    'compliment':"You look really pretty.",
                    'introduction': 'Hi, my name is',
                    'question': 'Do you know where I can have some copies of this document made?'
                },
                'reply':{
                    'compliment':["Thank you. Thats really nice of you to say.",-1],
                    'introduction': ["It's nice to meet you.",1],
                    'question': ["I'm too busy.",0],
                    'observation':['Yeah....', 0]
                }
            },
            2:{
                'statement':{
                    'compliment':"You look really pretty.",
                    'introduction': 'Hi, my name is',
                    'question': 'Do you know where I can have some copies of this document made?'
                },
                'reply':{
                    'compliment':["Thank you. Thats really nice of you to say.",0],
                    'introduction': ["Um.. That's nice.",1],
                    'question': ["Sure, the copy machine is right over here. I will show you.",1],
                    'observation':['Yeah....', 0]
                }
            },
            3:{
                'statement':{
                    'compliment':"You look really pretty.",
                    'introduction': 'Hi, my name is',
                    'question': 'Do you know where I can have some copies of this document made?'
                },
                'reply':{
                    'compliment':["Thank you. Thats really nice of you to say.",-1],
                    'introduction': ["Um.. That's nice.",1],
                    'question': ["I'm too busy.",0],
                    'observation':['Yeah....', 0]
                }
            },
            4:{
                'statement':{
                    'compliment':"You look really pretty.",
                    'introduction': 'Hi, my name is',
                    'question': 'Do you know where I can have some copies of this document made?'
                },
                'reply':{
                    'compliment':["Thank you. Thats really nice of you to say.",0],
                    'introduction':[ "Um.. That's nice.",1],
                    'question': ["I'm too busy.",0],
                    'observation':['Yeah....', 0],
                }
            }
        }
    },
    "liz":{
        "love":10,
        "prude":"easy",
        "location":"work",
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "jasmine":{
        "love":5,
        "prude":"hard",
        "location":"school",
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "claire":{
        "love": 10,
        "prude": "med",
        "location": ["shopping", "home"],
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "rebecca":{
        "love":5,
        "prude":"med",
        "location":"her_house",
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "brittany":{
        "love":5,
        "prude":"easy",
        "location": "home",
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "kerry":{
        "love":15,
        "prude":"hard",
        "location": ["river", "mountains"],
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "ricky":{
        "love":15,
        "prude":"med",
        "location":["gallery", "theatre"],
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    },
    "donika":{
        "love":10,
        "prude":"hard",
        "location":"gym",
        'opinion': 0,
        'affinity':'club',
        'dialogue_tree':{
            '01':{
                'question':"Hi my name is tammy. how are you?",
                'positive':"I like you.",
                'negative':"I don't like you."
            }
        }
    }
}