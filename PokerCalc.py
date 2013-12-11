from PokerRound import PokerRound
import numpy as np

d =2
p = 4
r = {'hand':25, 'base':8}

#print t.get_all_hands()

class PokerCalc():
    def __init__(self, decks, people, rules, n=10000):
        self.length = n
        self.hands = []
        for each in range(n):
            self.hands.append(PokerRound(decks, people, rules).get_all_hands())

    def get_sample_len(self):
        return self.length

    def __get_i_card_probability(self, card, number, player):
        occurance = 0
        for hand in self.hands:
            hand = hand[player]
            i = 0
            for e in hand:
                if e == card:
                    i = i+1
            if i == number:
                occurance = occurance+1
            
        return float(occurance)/float(self.length)

    def get_player_card_probability(self, card, number):
        return self.__get_i_card_probability(card, number, player = 0)
        
    def get_host_card_probability(self, card, number):
        return self.__get_i_card_probability(card, number, player = -1)

    def __get_i_sequence_probability(self, cards, player):
        occurance = 0
        for hand in self.hands:
            hand = hand[player] #player's cards in hand

            card_dict = {}
            for card in cards:
                card_dict.setdefault(card, 0)
                card_dict[card] = card_dict[card]+1

            for each in hand:
                if each in card_dict.keys():
                    if card_dict[each] > 0:
                        card_dict[each] = card_dict[each] - 1
            if np.sum(card_dict.values()) == 0:
                occurance = occurance + 1
        return float(occurance)/ float(self.length)

    def get_player_sequence_probability(self, cards):
        return self.__get_i_sequence_probability(cards, player = 0)

    def get_host_sequency_probability(self, cards):
        return self.__get_i_sequence_probability(cards, player = -1)
            

t = PokerCalc(d, p, r)

print t.get_sample_len()

print t.get_player_card_probability(1, 2)
print t.get_player_card_probability(2,3)
print t.get_player_card_probability(3,2)
print t.get_player_card_probability(54,1)

print t.get_player_sequence_probability([1,1,2,2])
print t.get_host_sequency_probability([1,1,2,2])

print t.get_host_card_probability(1,2)