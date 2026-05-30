class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
            ans = []
            def rec(index, sum, acc):
                if index == len(nums) or sum > target:
                    return
                if sum == target:
                    if not(acc in ans):
                        ans.append(acc.copy())
                        return
                acc.append(nums[index])
                rec(index, sum + nums[index], acc)
                acc.pop()
                rec(index + 1, sum, acc)
                
            rec(0,0,[])
            return ans