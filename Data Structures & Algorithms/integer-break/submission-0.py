class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp [1] = 0
        dp[2] =1
        for i in range(1,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i] , dp[i-j] * j , (i-j) * j)
        return dp[n]