class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count = Counter(hand)
        for i in range(len(hand)):
            start = hand[i]
            if(start not in count):
                continue
            for num in range(start, start + groupSize):
                if(num in count and count[num] > 0):
                    count[num] -= 1
                    if(count[num] == 0):
                        del count[num]
                else:
                    return False
        
        return len(count) == 0



