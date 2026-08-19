class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while j < len(prices):
            current_buy = prices[i]
            if prices[i] > prices[j] : # in this am saying don't buy and skip the buy
                # and take the next day to buy the thing taht i want to buy and go to the next day straight
                current_buy = prices[j]
                i = j
            profit = max(prices[j]-current_buy,profit)
            j = j + 1
        return profit

                
