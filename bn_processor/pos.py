import os
import json

class POS:

    def __init__(self):
        self.path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
        self.nouns = self._load_json(os.path.join(self.path , "bn_nouns.json"))
        self.pronouns = self._load_json(os.path.join(self.path , "bn_pronoun_list.json"))
        self.verbs = self._load_json(os.path.join(self.path , "bn_verbs.json"))




    def _load_json(self , path):

        with open(path) as f:
            return json.load(f)


    def get_pos_of(self , word):

        if word in self.nouns:
            return "noun"

        if word in self.pronouns:
            return "pronoun"


        if word in self.verbs:
            return "verb"

        return "noun"


