class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip duplicates
            target = -nums[i]  # nail it
            l = i + 1
            r = len(nums) - 1
            while l < r: # checking for the subarray on right of i
                curr_sum = nums[l] + nums[r]
                if curr_sum == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans   