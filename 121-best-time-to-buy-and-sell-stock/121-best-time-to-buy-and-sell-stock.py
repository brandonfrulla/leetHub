class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPurchase = prices[0]
        maxProfit = 0
        
        for price in prices:
            curProfit = price - minPurchase
            if curProfit > maxProfit:
                maxProfit = curProfit
            if price < minPurchase:
                minPurchase = price
                
        return maxProfit
        