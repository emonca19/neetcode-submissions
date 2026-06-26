class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSell = 0
        minBuy = prices[0]

        for sell in prices:
            minBuy = min(minBuy, sell)
            maxSell = max(maxSell, sell - minBuy)
        return maxSell
