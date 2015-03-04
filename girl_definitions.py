girl_list = {
    "tammy":{
        "love":15,
        "prude":"easy",
        "meet_at":"club",
        'affinity':'club',
        'meet_at':'bar',
        'dialogue_tree':{
            0:{
                'statement':{
                    'compliment':"Your work from last week was really good.",
                    'introduction': 'Hi, my name is',
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
        "meet_at":"work",
        'affinity':'restaurant',
        'dialogue_tree':{
            0:{
                'statement':{
                    'compliment':"Your work from last week was really good.",
                    'introduction': 'Hi, my name is',
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
    "jasmine":{
        "love":5,
        "prude":"hard",
        "meet_at":"school",
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
        "meet_at": 'shopping district',
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
        "meet_at":"store",
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
        "meet_at": "night life district",
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
        "meet_at": 'walking path',
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
        "meet_at": 'theatre district',
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
        "meet_at":"gym",
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