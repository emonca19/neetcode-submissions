class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r , res = 0, 1, 0
        
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(prices[r] - prices[l], res)
        return res


