class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[None] * n for _ in range(n)]
        
        def rec(l,r):
            if  l > r:
                return 0
            if dp[l][r] is not None:
                return dp[l][r]
            even = True if (r-l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            dp[l][r] = max(rec(l+1,r) + left, rec(l,r-1) + right)
            
            return dp[l][r]
        return rec(0,n-1) > 0