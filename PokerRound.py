import numpy as np
import math
#import argparse



#decks = 2
#people = 4

#rules = {'hand': 25, 'base': 8}

class PokerRound:

    def __init__(self, decks, people, rules, cards = []):
        self.decks = decks
        self.people = people
        self.rules = rules.copy()
        self.out_cards = cards[:]
        if self.rules['hand']*self.people+self.rules['base'] != self.decks * 54:
            print rules
            print self.rules
            print '[ERROR] invalid rules'
            quit()

        for e in self.out_cards:
            if e > 54:
                print '[ERROR] invalid out card'
                print e
                quit()
            
        self.cards = []

        for each in range(decks):
            self.cards = self.cards + list(range(1,55))

        if str(type(self.out_cards)) != "<type 'list'>":
            print '[ERROR] cards variable has to be a list'
            quit()
            
        l = len(self.out_cards)

        l = int(math.floor(float(l)/float(self.people)))

        if self.rules['hand'] <= l:
            print '[INFO] all cards are gone'
            quit()
        self.rules['hand'] = self.rules['hand'] - l

        self.__remove_cards()
        
        self.cards = np.array(self.cards)
        np.random.shuffle(self.cards)
        self.cards = self.__deal(c=self.cards, p = self.people, r= self.rules.copy())
        #self.rules = None

    def __remove_cards(self):
        for e1 in self.cards:
            if e1 in self.out_cards:
                self.cards[self.cards.index(e1)] = -1
                self.out_cards.remove(e1)
        self.cards =  [e for e in self.cards if e != -1]
        
        
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


if __name__ == '__main__':
    t = PokerRound(decks = 2, people = 4, rules = {'hand': 25, 'base': 8}, cards = [40,40, 51,52])
    print t.get_all_hands()