from functools import cmp_to_key

day = 7
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day{day}.txt').read().splitlines()

def getHandType(hand):
    counts = {x: 0 for x in '23456789TJQKA'}
    for char in hand: counts[char] += 1
    pairs = 0
    triples = 0
    fours = 0
    fives = 0
    for c in counts.keys():
        if counts[c] == 2: pairs += 1
        elif counts[c] == 3: triples += 1
        elif counts[c] == 4: fours += 1
        elif counts[c] == 5: fives += 1
    if fives == 1:
        type = 6
    elif fours == 1:
        type = 5
    elif triples == 1:
        if pairs == 1: type = 4
        else: type = 3
    elif pairs == 2:
        type = 2
    elif pairs == 1:
        type = 1
    else:
        type = 0
    return type

def getHandTypePart2(cards):
    actualType = getHandType(cards)
    if 'J' not in cards: return actualType
    elif cards == 'JJJJJ': return 6
    else:
        all_freq = {}
        for i in cards:
            if i != 'J':
                if i in all_freq:
                    all_freq[i] += 1
                else:
                    all_freq[i] = 1
        res = max(all_freq, key=all_freq.get)
        fixedHand = cards.replace('J', res)
        return getHandType(fixedHand)

def compareHands(hand1, hand2):
    ranks = '23456789TJQKA'
    type1, type2 = hand1[1], hand2[1]
    cards1, cards2 = hand1[0], hand2[0]
    if type1 > type2:
        return 1
    elif type1 < type2:
        return -1
    else:
        for char in range(len(cards1)):
            if ranks.index(cards1[char]) > ranks.index(cards2[char]):
                return 1
            elif ranks.index(cards1[char]) < ranks.index(cards2[char]):
                return -1
        return 0

def compareHandsPart2(hand1, hand2):
    ranks = 'J23456789TQKA'
    type1, type2 = hand1[1], hand2[1]
    cards1, cards2 = hand1[0], hand2[0]
    if type1 > type2:
        return 1
    elif type1 < type2:
        return -1
    else:
        for char in range(len(cards1)):
            if ranks.index(cards1[char]) > ranks.index(cards2[char]):
                return 1
            elif ranks.index(cards1[char]) < ranks.index(cards2[char]):
                return -1
        return 0

def part1():
    ranked = []
    sum = 0
    for line in f:
        hand = line.split()[0]
        bid = int(line.split()[1])
        type = getHandType(hand)
        ranked.append([hand, type, bid])
    # print(ranked)
    ranked.sort(key=cmp_to_key(compareHands))
    # print(ranked)
    for i in range(len(ranked)):
        # print(f'{ranked[i][2]} * {i+1}')
        sum += ranked[i][2] * (i+1)
    return sum

def part2():
    ranked = []
    sum = 0
    for line in f:
        hand = line.split()[0]
        bid = int(line.split()[1])
        type = getHandTypePart2(hand)
        ranked.append([hand, type, bid])
    # print(ranked)
    ranked.sort(key=cmp_to_key(compareHandsPart2))
    # print(ranked)
    for i in range(len(ranked)):
        # print(f'{ranked[i][2]} * {i+1}')
        sum += ranked[i][2] * (i+1)
    return sum

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
