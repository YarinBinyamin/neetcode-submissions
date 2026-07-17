class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def rec(acc, start):
            if start == len(nums):
                ans.append(acc.copy())
                return
            acc.append(nums[start])
            rec(acc,start+1)
            acc.pop()
            
            while start +1 < len(nums) and nums[start] == nums[start+1]:
                start+=1
            rec(acc,start+1)
        rec([],0)
        return ans
            