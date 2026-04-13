from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq_map = defaultdict(lambda: 0)
        for val in hand:
            freq_map[val] += 1

        for val in hand:
            if val in freq_map:
                count = 0
                right = val
                while count < groupSize:                        
                    if right in freq_map:
                        count += 1
                        freq_map[right] -= 1
                        if freq_map[right] == 0:
                            del freq_map[right]
                    else:
                        return False
                    right += 1
        return True
