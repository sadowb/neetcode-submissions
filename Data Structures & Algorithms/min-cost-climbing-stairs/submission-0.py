class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
   
        p0, p1 = cost[0], cost[1]  # Initialize with the cost of the first two steps
        
        for i in range(2, len(cost)):  # Start from the third step (index 2)
            current_cost = min(p0, p1) + cost[i]  # Min cost to reach the current step
            p0, p1 = p1, current_cost  # Move the pointers to the next two steps
        
        # The minimum cost to reach the top is the min of the last two steps
        return min(p0, p1)

