class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        def rec(i, acc):
            if acc not in ans:
                ans.append(acc.copy())
            if i > len(nums):
                return
            for j in range(i+1,len(nums)):
                acc.append(nums[j])
                rec(j,acc)
                acc.pop()
        rec(-1,[])
        return ans