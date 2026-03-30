class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp = 0
        buy = prices[0]

        for sell in prices:
            maxp = max(maxp,sell-buy)
            buy = min(buy,sell)

        return maxp        