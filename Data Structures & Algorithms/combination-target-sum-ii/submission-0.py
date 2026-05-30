class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def rec(index, acc, val):
            if val == target:
                if acc not in ans: # the order need to be important maybe set ? 
                    ans.append(acc.copy())
                    return
            if val > target or index >= len(candidates):
                return 
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                acc.append(candidates[i])
                rec(i+1,acc , val + candidates[i])
                acc.pop()
        rec(0,[],0) 
        return ans
