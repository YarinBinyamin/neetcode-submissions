class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m + n != len(s3):
            return False
        memo = [[None for _ in range(m+1)] for _ in range(n+1)]
        def rec(i , j  ):
            k = i+j
            if i == n and j == m and k == len(s3):
                    return True
            if memo[i][j] is not None:
                return memo[i][j]
            ans = False
            if i<n and s1[i] == s3[k]:
                ans = ans or rec(i+1,j)
            if j < m and s2[j] == s3[k]:
                ans = ans or rec(i,j+1)
            memo[i][j] = ans
            return memo[i][j]
        return rec(0,0)