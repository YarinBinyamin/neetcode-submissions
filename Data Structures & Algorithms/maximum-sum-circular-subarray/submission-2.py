class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, cur_sum = float("-inf"),0 
        l,r =0 ,0
        n = len(nums)
        total = 0
        while r < n:
            total+=nums[r]
            cur_sum+=nums[r]
            r+=1
            max_sum = max(max_sum,cur_sum)
            while cur_sum <0 and l<=r:
                cur_sum-=nums[l]
                l+=1
            
        #print(max_sum)
        #print(total)
        l,r =0 ,0
        cur_sum = 0
        min_sum = float("inf")
        while r < n:
            cur_sum+=nums[r]
            r+=1
            min_sum = min(min_sum, cur_sum)
            while cur_sum > 0 and l <= r:
                cur_sum-= nums[l]
                l+=1
            
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)