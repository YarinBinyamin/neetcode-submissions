class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            memo = [None] * len(cost)
            def rec(index):
                if index >= len(cost):
                    return 0  
                if memo[index] != None:
                    return memo[index]
                memo[index] = cost[index] + min(rec(index+1), rec(index+2))
                return memo[index] 
            return min(rec(0), rec(1))