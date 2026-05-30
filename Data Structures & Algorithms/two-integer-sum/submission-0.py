class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen =  {}
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            if nums[i] in seen:
                return [seen[nums[i]] , i]
            dif = target - nums[i]
            seen[dif] = i