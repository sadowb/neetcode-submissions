class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = 0
        
        # Iterate over the number of 2-steps (y) from 0 to n // 2
        for y in range(n // 2 + 1):
            x = n - 2 * y  # Remaining steps must be 1-steps
            total_ways += math.comb(x + y, y)  # Binomial coefficient C(x + y, y)

        return total_ways