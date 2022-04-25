class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #must start on "day 1", can't get any cheaper than day 1 to start
        minPurchase = prices[0]
        maxProfit = 0
        
        for price in prices:
            curProfit = price - minPurchase
            #save new profit, if more is made on this trade than previous high
            if curProfit > maxProfit:
                maxProfit = curProfit
            #adjust buy-in to new lower price, when one is found
            if price < minPurchase:
                minPurchase = price
                
        return maxProfit
        