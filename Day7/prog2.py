
#camelcards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
camelcards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


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
        self.Jcards = cards
        self.bids = int(bids)
        self.lcount = []
        self.lcount[0:] = [0] * (len(camelcards))

def return_indeces(my_list, item, cards):
    count = [i for i in range(len(my_list)) if my_list[i] == item]
    return count

def replace_card_joker(cb):
    indexI = 0
    while indexI < len(cb.cards):
        cb.lcount[camelcards.index(cb.cards[indexI])] += 1
        indexI += 1
    print(cb.lcount)

    #if cb.cards[0] == cb.cards[1] == cb.cards[2] == cb.cards[3] == cb.cards[4] == "J": # "JJJJJ"
    #    cb.Jcards = "AAAAA"
    if len(return_indeces(cb.lcount, 4, cb.cards)) == 1:
        index = cb.lcount.index(4)
        if camelcards[index] == "J":
            index = cb.lcount.index(1)
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])
        else:
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])

    elif len(return_indeces(cb.lcount, 3, cb.cards)) == 1:
        index = cb.lcount.index(3)
        if camelcards[index] == "J":
            if 2 in cb.lcount:
                index = cb.lcount.index(2)
                cb.Jcards = cb.Jcards.replace("J", camelcards[index])
            else:
                index = cb.lcount.index(1) # To check here which to pick - higher or lower
                cb.Jcards = cb.Jcards.replace("J", camelcards[index])
        else:
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])
            print(str(index) + " " + camelcards[index] + " " + cb.cards + " " + cb.Jcards)

    elif len(return_indeces(cb.lcount, 2, cb.cards)) == 1:
        index = cb.lcount.index(2)
        if camelcards[index] == "J":
            index = cb.lcount.index(1)
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])
        else:
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])

    elif len(return_indeces(cb.lcount, 2, cb.cards)) == 2:
        indeces = [i for i in range(len(cb.lcount)) if cb.lcount[i] == 2]
        print(indeces)
        if camelcards[indeces[0]] == "J": # "JJQAA"
            index = indeces[1]
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])
        elif camelcards[indeces[1]] == "J": # "AAQJJ"
            index = indeces[0]
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])
        else: # "AAKQQ"
            index = indeces[0]
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])

    else:
        indeces = [i for i in range(len(cb.lcount)) if cb.lcount[i] == 1]
        if indeces:
            print("cb.lcount[i] == 1 " + cb.Jcards + " " + cb.cards)
            index = indeces[0]
            cb.Jcards = cb.Jcards.replace("J", camelcards[index])

    print("replaced: " + cb.cards + " " + cb.Jcards)

def check_diff_index_input(input1, input2, index):
    return camelcards.index(input1[index]) - camelcards.index(input2[index])

def get_rank(input1, input2):
    print(input1 + " " + input2)
    index = 0
    while index < len(input1):
        diff = check_diff_index_input(input1, input2, index)
        if diff == 0:
            index += 1
        else:
            return diff
    return 0 # Both are same

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
    cb.lcount[0:] = [0] * (len(camelcards))
    indexI = 0
    while indexI < len(cb.Jcards):
        cb.lcount[camelcards.index(cb.Jcards[indexI])] += 1
        indexI += 1

    #print(cb.cards)
    if cb.Jcards[0] == cb.Jcards[4] == cb.Jcards[1] == cb.Jcards[3] == cb.Jcards[2]:
        # Five of a kind
        print("Five of a kind")
        insert_object(FIVEKIND, cb)

    elif len(return_indeces(cb.lcount, 4, cb.Jcards)) == 1:
        # Four of a kind
        print("Four of a kind")
        insert_object(FOURKIND, cb)
    elif (len(return_indeces(cb.lcount, 3, cb.Jcards)) == 1) and (len(return_indeces(cb.lcount, 2, cb.Jcards)) == 1):
        # Full house
        print("Full house")
        insert_object(FULLHOUSE, cb)
    else:
        # 3 + 1 + 1     - Three of a kind (3 + 2 also possible)
        # 2 + 2 + 1     - Two pair
        # 2 + 1 + 1 + 1 - One pair
        # All one       - High card
        if len(return_indeces(cb.lcount, 3, cb.Jcards)) == 1:
            # Three of a kind
            print("Three of a kind")
            insert_object(THREEKIND, cb)
        elif len(return_indeces(cb.lcount, 2, cb.Jcards)) == 2:
            # Two pair
            print("Two pair")
            insert_object(TWOPAIR, cb)
        elif len(return_indeces(cb.lcount, 1, cb.Jcards)) == 3:
            # One pair
            print("One pair")
            insert_object(ONEPAIR, cb)
        elif len(return_indeces(cb.lcount, 1, cb.Jcards)) == 5:
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
        print(cb.cards + ":" + cb.Jcards, end=" ")
    print()

# Main starts here
inputfp = open('input.txt', 'r')

while True:
    s1 = inputfp.readline().strip()
    if not s1:
        break
    line = s1.split(" ")
    cb = CardsBids(line[0], line[1])
    replace_card_joker(cb)
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
