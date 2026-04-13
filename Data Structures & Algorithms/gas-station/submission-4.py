class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff, curr_diff = 0, 0
        start = 0
        for i in range(len(gas)):
            diff = (gas[i] - cost[i])
            total_diff += diff
            curr_diff += diff
            if curr_diff < 0:
                start = i + 1
                curr_diff = 0
        return start if total_diff >= 0 else -1
