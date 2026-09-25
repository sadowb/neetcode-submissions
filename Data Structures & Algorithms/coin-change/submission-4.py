class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(remaining):
            if remaining == 0:
                return 0
            if remaining < 1:
                return amount + 1
            if remaining in memo:
                return memo[remaining]
            best = amount + 1
            
            for coin in coins:
                best = min(best,1 + solve(remaining - coin))
        
            memo[remaining] = best
            return best
        result = solve(amount)

        return -1 if result == amount + 1 else result
