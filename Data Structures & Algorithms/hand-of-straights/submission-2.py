from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq_map = Counter(hand)

        for val in sorted(hand):
            if freq_map[val] > 0: 
                count = freq_map[val]
                for i in range(val, val + groupSize):
                    if freq_map[i] < count:
                        return False
                    else:
                        freq_map[i] -= count
        return True
