class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
            def rec(cur_sum, index):
                if index == len(nums):
                    if cur_sum == target:
                        return 1
                    return 0
                total = rec(cur_sum + nums[index], index+1) + rec(cur_sum - nums[index], index+1)
                return total   
            return  rec(0,0) 