
camelcards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


import re


FIVEKIND = []
FOURKIND = []
FULLHOUSE = []
THREEKIND = []
TWOPAIR = []
ONEPAIR = []
HIGHCARD = []

class CardsBids:
    def __init__(self, cards, bids):
        self.cards = cards
        self.bids = int(bids)
        self.lcount = []
        self.lcount[0:] = [0] * (len(camelcards))

def return_indeces(my_list, item):
    return [i for i in range(len(my_list)) if my_list[i] == item]

def check_diff_index_input(input1, input2, index):
    return camelcards.index(input1[index]) - camelcards.index(input2[index])

def get_rank(input1, input2):
    index = 0
    while index < len(input1):
        diff = check_diff_index_input(input1, input2, index)
        if diff == 0:
            index += 1
        else:
            return diff

def insert_object(OBJECT_TYPE, cb):
    if len(OBJECT_TYPE) == 0:
        OBJECT_TYPE.insert(0, cb)
        return
    else:
        inserted = False
        for index in range(len(OBJECT_TYPE)):
            obj = OBJECT_TYPE[index]
            if (get_rank(obj.cards, cb.cards)) < 0:
                OBJECT_TYPE.insert(index, cb)
                inserted = True
                break
        if not inserted:
            OBJECT_TYPE.append(cb)

def check_cards(cb):
    indexI = 0
    while indexI < len(cb.cards):
        cb.lcount[camelcards.index(cb.cards[indexI])] += 1
        indexI += 1

    print(cb.cards)
    if cb.cards[0] == cb.cards[4] == cb.cards[1] == cb.cards[3] == cb.cards[2]:
        # Five of a kind
        print("Five of a kind")
        insert_object(FIVEKIND, cb)

    elif len(return_indeces(cb.lcount, 4)) == 1:
        # Four of a kind
        print("Four of a kind")
        insert_object(FOURKIND, cb)
    elif (len(return_indeces(cb.lcount, 3)) == 1) and (len(return_indeces(cb.lcount, 2)) == 1):
        # Full house
        print("Full house")
        insert_object(FULLHOUSE, cb)
    else:
        # 3 + 1 + 1     - Three of a kind (3 + 2 also possible)
        # 2 + 2 + 1     - Two pair
        # 2 + 1 + 1 + 1 - One pair
        # All one       - High card
        if len(return_indeces(cb.lcount, 3)) == 1:
            # Three of a kind
            print("Three of a kind")
            insert_object(THREEKIND, cb)
        elif len(return_indeces(cb.lcount, 2)) == 2:
            # Two pair
            print("Two pair")
            insert_object(TWOPAIR, cb)
        elif len(return_indeces(cb.lcount, 1)) == 3:
            # One pair
            print("One pair")
            insert_object(ONEPAIR, cb)
        elif len(return_indeces(cb.lcount, 1)) == 5:
            # High card
            print("All one")
            insert_object(HIGHCARD, cb)

def get_total_winnings(OBJECT_TYPE):
    index = 0
    total = 0
    while index < len(OBJECT_TYPE):
        cb = OBJECT_TYPE[index]
        print(str(total) + " " + str(cb.bids))
        total += cb.bids * (index + 1)
        index += 1
    return total

def print_values_obj(OBJECT_TYPE):
    for cb in OBJECT_TYPE:
        print(cb.cards, end=" ")
    print()

# Main starts here
inputfp = open('input.txt', 'r')

while True:
    s1 = inputfp.readline().strip()
    if not s1:
        break
    line = s1.split(" ")
    cb = CardsBids(line[0], line[1])
    check_cards(cb)

inputfp.close()

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
print("FIVEKIND")
print_values_obj(FIVEKIND)
print("FOURKIND")
print_values_obj(FOURKIND)
print("FULLHOUSE")
print_values_obj(FULLHOUSE)
print("THREEKIND")
print_values_obj(THREEKIND)
print("TWOPAIR")
print_values_obj(TWOPAIR)
print("ONEPAIR")
print_values_obj(ONEPAIR)
print("HIGHCARD")
print_values_obj(HIGHCARD)
ALLKINDLIST = HIGHCARD + ONEPAIR + TWOPAIR + THREEKIND + FULLHOUSE + FOURKIND + FIVEKIND


total = get_total_winnings(ALLKINDLIST)
print("Total " + str(total))
