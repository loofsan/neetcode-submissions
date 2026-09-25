class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        mostProfit = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            elif prices[r] > prices[l]:
                mostProfit = max(mostProfit, prices[r] - prices[l])
            r+=1

        return mostProfit
            
