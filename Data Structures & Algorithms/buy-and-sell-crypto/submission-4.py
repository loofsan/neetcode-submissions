class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        biggestProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                biggestProfit = max(currProfit, biggestProfit)
            else:
                l = r
            r += 1
            
        return biggestProfit