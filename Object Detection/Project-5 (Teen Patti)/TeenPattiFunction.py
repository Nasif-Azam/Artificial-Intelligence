TeenPattiHandRanks = {6: "Trio(3 of a Kind)", 5: "Pure Sequence(Straight Flush)",
                  4: "Sequence(Straight)", 3: "Color(Flush)",
                  2: "Pair", 1: "High Card"}


def findTeenPattiHand(hand):
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
    if suits.count(suits[0]) == 3:
        # Pure Sequence(Straight Flush)
        if all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(5)
        # Color(Flush)
        else:
            possibleRanks.append(3)
    # Sequence(Straight)
    # 10 11 12
    # 11 == 10+1, 12 == 11 +1 True
    # 11 == 7+1 False
    if all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(4)

    handUniqueValues = list(set(sortedRanks))

    # Trio(3 of a Kind)
    # 3 3 3 -- Set -- 3 -- Unique Values -- 1 -- Trio Three of a Kind
    if len(handUniqueValues) == 1:
        for values in handUniqueValues:
            if sortedRanks.count(values) == 3:
                possibleRanks.append(6)

    # print(handUniqueValues)
    # 3 of a Kind
    # 5 5 5 6 7 -- Set -- 5 6 7 -- Unique Values -- 3 -- Three of a Kind

    # if len(handUniqueValues) == 2:
    #     for values in handUniqueValues:
    #         if sortedRanks.count(values) == 3:
    #             possibleRanks.append(4)
            # 2 pair
            # 8 8 7 7 2 -- Set -- 8 7 2 -- Unique Values -- 3 -- Two Pair

            # if sortedRanks.count(values) == 2:
            #     possibleRanks.append(3)
    # Pair
    # 5 5 8 -- Set -- 5 8 -- Unique Values -- 2 -- Pair
    if len(handUniqueValues) == 2:
        for values in handUniqueValues:
            if sortedRanks.count(values) == 2:
                possibleRanks.append(2)
    #High Card
    if not possibleRanks:
        possibleRanks.append(1)
            # print("Royal Flush")
    # print(possibleRanks)
    # pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind",
    #                   7: "Full House", 6: "Flush", 5: "Straight", 4: "Three of a Kind",
    #                   3: "Two Pair", 2: "Pair", 1: "High Card"}
    # pokerHandRanks = {6: "Trio(3 of a Kind)", 5: "Pure Sequence(Straight Flush)",
    #                   4: "Sequence(Straight)", 3: "Color(Flush)",
    #                   2: "Pair", 1: "High Card"}
    output = TeenPattiHandRanks[max(possibleRanks)]
    print(hand, output)
    # print(output)
    return output

if __name__ == '__main__':
    findTeenPattiHand(["AH", "AS", "AD"])  # Trio(3 of a Kind)
    findTeenPattiHand(["9C", "10C", "JC"])  # Pure Sequence(Straight Flush)
    findTeenPattiHand(["QH", "KS", "AD"])  # Sequence(Straight)
    findTeenPattiHand(["8H", "6H", "10H"])  # Color(Flush)
    findTeenPattiHand(["10D", "6H", "6S"])  # Pair
    findTeenPattiHand(["KC", "8H", "3S"])  # High card
