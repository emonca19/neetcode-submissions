class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, minBuy, maxSell = 0, prices[0], 0

        res = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r 
                minBuy = min(minBuy, prices[r])
                maxSell = max(prices[l], prices[r])
                
            else:
                maxSell = max(maxSell, prices[r])
                res = max(res, maxSell - minBuy)
        
        return res

