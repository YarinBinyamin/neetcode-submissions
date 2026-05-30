class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        n = len(nums)
        max_all = nums[0]
        for i in range(1,n):
            print(f"current = {current}  | nums[{i}] = {nums[i]} | both = {current + nums[i]}")
            current = max(nums[i], current + nums[i])
            max_all = max(max_all,current)
        return max_all