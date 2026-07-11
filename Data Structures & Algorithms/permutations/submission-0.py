class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def rec(acc):
            if len(acc) == n :
                if acc not in ans:
                    ans.append(acc.copy())
                    return
            for e in nums:
                if e not in acc:
                    acc.append(e)
                    rec(acc)
                    acc.remove(e)
        rec([])
        return ans
                    