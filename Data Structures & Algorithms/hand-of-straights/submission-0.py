from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        freqs = defaultdict(int)
        for c in hand:
            freqs[c] += 1
        for i in range(len(hand)):
            if hand[i] not in freqs:
                continue
            notFound = False
            for val in range(hand[i], hand[i]+groupSize):
                if val not in freqs:
                    notFound = True
                    break
                freqs[val] -= 1
                if freqs[val] == 0:
                    del freqs[val]
            if notFound:
                return False
        return True