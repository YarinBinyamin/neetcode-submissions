class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        def rob_liner(start,end):
            dp = [0] * (len(nums)) 
            for i in range(start,end+1):
                dp[i] = max(nums[i]+(dp[i-2] if i-2 >=0 else 0), dp[i-1] if i-1 >=0 else 0)
            return dp[end]
        return max( rob_liner(0,len(nums) -2),rob_liner(1,len(nums) -1) )
                