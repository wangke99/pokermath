import numpy as np
#import argparse



#decks = 2
#people = 4

#rules = {'hand': 25, 'base': 8}

class PokerRound:

    def __init__(self, decks, people, rules):
        self.cards = []

        for each in range(decks):
            self.cards = self.cards + list(range(1,55))
    
        self.cards = np.array(self.cards)
        np.random.shuffle(self.cards)
        self.cards = self.__deal(c=self.cards, p = people, r= rules)

    def get_all_hands(self):
        return self.cards

    def get_host_hand(self):
        return self.cards[-1]

    def __deal(self, c, p, r):
        hand = r['hand']
        base = r['base']
        deals = []
        for each in range(p-1):
            deals.append(list(c[each*hand:(each+1)*hand]))
        deals.append(list(c[(p-1)*hand:]))
        return deals
