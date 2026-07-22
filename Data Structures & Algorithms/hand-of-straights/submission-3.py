from collections import deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freqs = Counter(hand)
        for c in sorted(freqs):
            ct = freqs[c]
            if ct > 0:
                for i in range(groupSize):
                    if freqs[c + i] <= 0:
                        return False
                    freqs[c + i] -= ct
        return True

        
        # if len(hand) % groupSize != 0:
        #     return False
        # hand.sort()
        # groups = defaultdict(deque)
        # for c in hand:
        #     length = 1
        #     if c-1 in groups:
        #         length = groups[c-1].popleft() + 1
        #         if len(groups[c-1]) == 0:
        #             del groups[c-1]
        #     if length < groupSize:
        #         groups[c].append(length)
        # return not groups
"""
1, 2, 2, 3, 3, 4, 4, 5





"""
                
        # if len(hand) % groupSize != 0:
        #     return False
        # hand.sort()
        # freqs = defaultdict(int)
        # for c in hand:
        #     freqs[c] += 1
        # for i in range(len(hand)):
        #     if hand[i] not in freqs:
        #         continue
        #     notFound = False
        #     for val in range(hand[i], hand[i]+groupSize):
        #         if val not in freqs:
        #             notFound = True
        #             break
        #         freqs[val] -= 1
        #         if freqs[val] == 0:
        #             del freqs[val]
        #     if notFound:
        #         return False
        # return True