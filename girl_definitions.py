girl_list = {
    "tammy":{
        "love":15,
        "prude":"easy",
        'affinity':'club',
        'meet_at':'bar',
        'see_at':['bar', 'night life district', 'historic district'],
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
        'meet_at':'work',
        "see_at":["work", 'city', 'shopping district'],
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
        'meet_at':'school',
        "see_at":["school", 'walking path', 'historic district'],
        'affinity':'club', #??
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
    "claire":{
        "love": 10,
        "prude": "med",
        'meet_at':'shopping district',
        "see_at": ['shopping district', 'store', 'historic district'],
        'affinity':'club',
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
    "rebecca":{
        "love":5,
        "prude":"med",
        'meet_at':'store',
        "see_at":['shopping district', "store", 'city'],
        'affinity':'club',
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
    "brittany":{
        "love":5,
        "prude":"easy",
        'meet_at':'night life district',
        "see_at": ["night life district", 'bar','city'],
        'affinity':'club',
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
    "kerry":{
        "love":15,
        "prude":"hard",
        'meet_at':'hiking trails',
        "see_at": ['walking path','hiking trails', 'historic district'],
        'affinity':'club',
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
    "ricky":{
        "love":15,
        "prude":"med",
        'meet_at':'theatre district',
        "see_at": ['theatre district','school','city'],
        'affinity':'club',
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
    "donika":{
        "love":10,
        "prude":"hard",
        'meet_at':'gym',
        "see_at":["gym",'work', 'historic district'],
        'affinity':'club',
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
    }
}