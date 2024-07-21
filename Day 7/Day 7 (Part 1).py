fhand = open("Input.txt")
cards_bids = dict()
type_5 = list()
type_4 = list()
type_house = list()
type_3 = list()
type_twopair = list()
type_2 = list()
type_1 = list()
types = (type_5, type_4, type_house, type_3, type_twopair, type_2, type_1)
cards_rank = dict()

# Filling the dict with each card and bid
for line in fhand:
    cards_bids[line.split()[0]] = line.split()[1]

# Creating 7 different lists for each type
for card in cards_bids:

    # Dictionary 'bag' to count number of repeats
    bag = dict()
    for letter in card:
        bag[letter] = bag.get(letter, 0) + 1
    
    # Sorting into types
    card_type = sorted(list(bag.values()), reverse=True)
    if card_type[0] == 5:
        types[0].append(card)
    elif card_type[0] == 4:
        types[1].append(card)
    elif card_type[0] == 3 and card_type[1] == 2:
        types[2].append(card)
    elif card_type[0] == 3 and card_type[1] == 1:
        types[3].append(card)
    elif card_type[0] == 2 and card_type[1] == 2:
        types[4].append(card)
    elif card_type[0] == 2 and card_type[1] == 1:
        types[5].append(card)
    elif card_type[0] == 1:
        types[6].append(card)

# Defining sort key for second round of sorting
def sort_cards(x):
    cheat_sheet = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    points = 0
    pos = 10000000000
    for letter in x:
        points += cheat_sheet[letter]*pos
        pos /= 100
    return(points)

for t in types:
    t.sort(key=sort_cards, reverse=True)

# Matching rank with bid
n = 1000
for t in types:
    for card in t:
        cards_rank[card] = n
        n -= 1

# Calculating total winnings
total_winnings = 0
for i in cards_rank:
    total_winnings += cards_rank[i]*int(cards_bids[i])

print(total_winnings)