
def findPokerHand(hand):
    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        # print(f'Rank: {rank}    Suit: {suit}')

        if rank == "A": rank = 14
        elif rank == "K": rank = 13
        elif rank == "Q": rank = 12
        elif rank == "J": rank = 11
        # elif rank == "10": rank = 10

        ranks.append(int(rank))
        suits.append(suit)
    # print(ranks)
    sortedRanks = sorted(ranks)
    # print(sortedRanks)
    # Flush
    if suits.count(suits[0]) == 5:
        # Royal Flush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks\
                and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10)
        # Straight Flush
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)
        # Flush
        else:
            possibleRanks.append(6)
    # Straight
    # 10 11 12 13 14
    # 11 == 10+1, 12 == 11 +1 True
    # 11 == 7+1 False
    if all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueValues = list(set(sortedRanks))

    # 4 of a Kind
    # 3 3 3 3 5 -- Set -- 3 5 -- Unique Values -- 2 -- Four of a Kind
    if len(handUniqueValues) == 2:
        for values in handUniqueValues:
            if sortedRanks.count(values) == 4:
                possibleRanks.append(8)
                # Full House
                # 3 3 3 5 5 -- Set -- 3 5 -- Unique Values -- 2 -- Full House
            elif sortedRanks.count(values) == 3: # If uses
                possibleRanks.append(7)
    # print(handUniqueValues)
    # 3 of a Kind
    # 5 5 5 6 7 -- Set -- 5 6 7 -- Unique Values -- 3 -- Three of a Kind
    if len(handUniqueValues) == 3:
        for values in handUniqueValues:
            if sortedRanks.count(values) == 3:
                possibleRanks.append(4)
            # 2 pair
            # 8 8 7 7 2 -- Set -- 8 7 2 -- Unique Values -- 3 -- Two Pair
            if sortedRanks.count(values) == 2:
                possibleRanks.append(3)
    # Pair
    # 5 5 8 6 7 -- Set -- 5 8 6 7 -- Unique Values -- 4 -- Pair
    if len(handUniqueValues) == 4:
        for values in handUniqueValues:
            if sortedRanks.count(values) == 2:
                possibleRanks.append(2)
    #High Card
    if not possibleRanks:
        possibleRanks.append(1)
            # print("Royal Flush")
    # print(possibleRanks)
    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind",
                      7: "Full House", 6: "Flush", 5: "Straight", 4: "Three of a Kind",
                      3: "Two Pair", 2: "Pair", 1: "High Card"}
    output = pokerHandRanks[max(possibleRanks)]
    print(hand, output)
    return output

if __name__ == '__main__':
    findPokerHand(["KH", "AH", "QH", "JH", "10H"])  # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # 4 of a Kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # 3 of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # 2 Pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High card
