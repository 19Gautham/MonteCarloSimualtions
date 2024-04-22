import numpy as np
from _collections import OrderedDict

class questionDos(object):
    
    def __init__(self):
        self.hands = {}
        self.hands["Straight Flush"] = 0
        self.hands["Full House"] = 0
        self.hands["Flush"] = 0
        self.hands["Straight"] = 0
        self.hands["Three of a Kind"] = 0
        self.hands["Two Pair"] = 0
        self.hands["One Pair"] = 0
        self.hands["No Pair"] = 0
        
        # Spades, Hearts, Diamonds
        self.suits = ["S", "H", "D"]
        self.card_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.card_count = OrderedDict()
        for key in self.card_names:
            self.card_count[key] = 0

        # This structure is used to define the deck of cards
        # Essentially an array contain cards in the format 2S - 2 of Spades, and so on and so forth
        self.cards = [card+suit for card in self.card_names for suit in self.suits]

    """
        This function is used to generate a 5 card hand randomly from the deck of 36 cards
    """
    def generate_hand(self):
        return np.random.choice(self.cards, size=5, replace=False)

    """
        This function is used to determine if the hand can be classified as a straight
        The logic below essentially uses the property of the ordered dictionary to find
        the highest and lowest index of the cards in the hand and see if it equals 4 + 1
        in order to check if they are sequential, which essentially is the criteria for a
        Straight
    """
    def is_straight_hand(self, hand_count):
        i = 0
        item_list = list(hand_count.items())
        # print("Hand Count: {}".format(item_list))
        while i < len(item_list) and not item_list[i][1] > 0:
            i += 1
        low = i
        while i < len(item_list) and item_list[i][1] > 0:
            i += 1
        high = i
        
        return high - low == 5       
        
            
    """
        This function is used to define the rules to classify each poekr hand
    """
    def classify_hand(self, hand):
        
        #Store the unique (by virtue of using the set data structure in python) suites of all cards in a hand
        suits = set()
        hand_count = self.card_count.copy()

        for card in hand:
            # add the suite to the set
            suits.add(card[len(card)-1])
            # increase the count of a particular rank of card
            hand_count[card[:len(card)-1]] += 1

        # Number of pairs
        pair_count = sum(val == 2 for val in hand_count.values())

        # straight flush
        if len(suits) == 1 and self.is_straight_hand(hand_count):
            self.hands["Straight Flush"] += 1
        elif 3 in hand_count.values() and 2 in hand_count.values():
            self.hands["Full House"] += 1
        elif len(suits) == 1 and not self.is_straight_hand(hand_count):
            self.hands["Flush"] += 1
        elif self.is_straight_hand(hand_count) and len(suits) > 1:
            self.hands["Straight"] += 1
        # It is a 5 card hand so we don't need to worry about there being multiple 3 values
        elif any(val == 3 for val in hand_count.values()):
            self.hands["Three of a Kind"] += 1
        elif pair_count == 2:
            self.hands["Two Pair"] += 1
        elif pair_count == 1:
            self.hands["One Pair"] += 1
        else:
            self.hands["No Pair"] += 1

    def generate_poker_hand_report(self, iterations):
        print("Hand probabilities\n\n")
        for key in self.hands.keys():
            print("Number of {}: {}".format(key, self.hands[key]))
            print("{} probability: {}%".format(key, (self.hands[key] * 100)/iterations))

    def calculate_poker_hand_probability(self):
        
        iterations = 4000000
        for _ in range(iterations):
            hand = self.generate_hand()
            self.classify_hand(hand)             
        
        self.generate_poker_hand_report(iterations)

if __name__ == "__main__":
    dos = questionDos()
    dos.calculate_poker_hand_probability()
