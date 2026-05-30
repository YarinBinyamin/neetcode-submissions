class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]* n
        def rec(pos ):
            if pos== n:
                return 1
            if pos > n :
                return 0 
            if memo[pos] != -1:
                return memo[pos]
            memo[pos] = rec(pos +1) + rec(pos +2)
            return memo[pos]
        return rec(0)