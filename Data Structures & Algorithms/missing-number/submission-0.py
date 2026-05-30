class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_of_nums = 0
        sum_of_n = 0
        for e in nums:
            sum_of_nums +=e
        for i in range(len(nums)+1):
            sum_of_n +=i
        return sum_of_n - sum_of_nums