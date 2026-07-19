class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len  = float('inf')
        sum_cur = 0
        l,r = 0,0
        n = len(nums)
        while r < n:
            sum_cur += nums[r]
            r+=1
            while sum_cur >= target:
                min_len = min ( min_len, r-l)
                sum_cur -=nums[l]
                l+=1
        if min_len == float('inf'):
            return 0
        return min_len