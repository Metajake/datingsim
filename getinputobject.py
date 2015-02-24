#object version

#Parser Error Function  
class ParserError(Exception):
    pass

#The final Sentence Class outputted by the parser functions
class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

#Input Object
class Input(object):
    def __init__(self):
        #self.verb=['go','give','leave','use','look','reflect']
        #self.direction=['north','south','east','west','inside', 'outside']
        self.verb = []
        self.direction = []
        self.noun=['condom','flowers']
        self.stop=['the','in','of','to', 'at']
        self.vocab={
            'verb':self.verb,
            'direction':self.direction,
            'noun':self.noun,
            'stop':self.stop
        }

    def scan(self, sentence, inputobj):
        """Input the raw text --> Output a List of Tuples which correspond to the categories above"""
        wordlist=sentence.split()
        result=[]
        for word in wordlist:
            found=False
            for key,value in inputobj.vocab.items():
                if word.lower() in value:
                    result.append((key,word))
                    found=True
                    break
            if not found:
                try:
                    word=int(word)
                    result.append(('number',word))
                except ValueError:
                    result.append(('error',word))
        return result
                
    def peek(self, word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None
                
    def match(self, word_list, expecting):
        if word_list:
            word = word_list.pop(0)
            
            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None
        
    def skip(self, word_list, word_type):
        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)
    
    def parse_subject(self, word_list):
        self.skip(word_list, 'stop')
        next_word = self.peek(word_list)
        
        if next_word == 'noun':
            return self.match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("(parsing subject) Expected a verb next.")
                
    def parse_verb(self, word_list):
        self.skip(word_list, 'stop')
        
        if self.peek(word_list) == 'verb':
            return self.match(word_list, 'verb')
        else:
            raise ParserError("(parsing verb) Expected a verb next.")
                
    def parse_object(self, word_list):
        self.skip(word_list, 'stop')
        next_word = self.peek(word_list)
        
        if next_word == 'noun':
            return self.match(word_list, 'noun')
        elif next_word == 'direction':
            return self.match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")
            
    def parse_sentence(self, word_list):
        subj = self.parse_subject(word_list)
        verb = self.parse_verb(word_list)
        obj = self.parse_object(word_list)
        return Sentence(subj, verb, obj)