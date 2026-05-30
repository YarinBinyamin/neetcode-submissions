class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        memo = [[None for _ in range(m)] for _ in range(n)]
        def rec(i,j):
            if i == n :
                return True
            elif j == m and i < n:
                return False
            if memo[i][j] != None:
                return memo[i][j]
            if s[i] == t[j]:
                memo[i][j] = rec(i+1,j+1)
            else:   
                memo[i][j] = rec(i, j + 1)
            return memo[i][j]
        return rec(0,0)