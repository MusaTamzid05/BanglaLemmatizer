from bn_processor.pos import POS
from banglakit.lemmatizer import BengaliLemmatizer

class BanglaLemmatizer:

    def __init__(self):
        self.pos_getter = POS()
        self.lemmatizer = BengaliLemmatizer()

    def lemmatize(self , word , pos = None):

        if pos is None:
            pos = self.pos_getter.get_pos_of(word)

        res = self.lemmatizer.lemmatize(word , pos = pos)

        if res == "-PRON-":
            res = word

        return res




