class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for e in nums:
            total +=e
        if total % 2 !=0:
            return False 
        t = total // 2
        dp = [[None for _ in range(t+1)] for _ in range(len(nums))]
        def rec(i, val):
            if val == 0 :
                return True
            if i >= len(nums) or val < 0:
                return False
            if dp[i][val] is not None:
                return dp[i][val]
            dp[i][val] = rec(i+1,val-nums[i]) or rec(i+1,val)
            return dp[i][val]
        return rec(0,t)