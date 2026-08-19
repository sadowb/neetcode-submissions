class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                current = prices[j] - prices[i]
                if current >= profit:
                    profit = current
        return profit
                
        
        
        