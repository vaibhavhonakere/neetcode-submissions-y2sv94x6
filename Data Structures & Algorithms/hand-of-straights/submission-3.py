class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count = Counter(hand)
        for h in hand:
            if(h not in count):
                continue
            for card in range(h, h + groupSize):
                if(card in count and count[card] > 0):
                    count[card] -= 1
                    if(count[card] == 0):
                        del count[card]
                else:
                    return False
        
        return len(count) == 0



