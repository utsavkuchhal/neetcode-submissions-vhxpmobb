class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def solve(index, can_buy):
            if index >= len(prices):
                return 0
            if (index, can_buy) in memo:
                return memo[(index, can_buy)]

            if can_buy:
                buy = - prices[index] + solve(index + 1, False) 
                skip = solve(index + 1, True)
                profit = max(buy, skip)
            else:
                sell =  prices[index] + solve(index + 2, True)
                hold = solve(index + 1, False)
                profit = max(sell, hold)

            memo[(index, can_buy)] = profit
            return profit
        return solve(0, True)