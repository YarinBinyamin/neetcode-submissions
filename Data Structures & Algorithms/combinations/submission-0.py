class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
            ans = []
            def rec(acc : set(),start):
                if len(acc) == k:
                    if acc not in ans:
                        ans.append(acc.copy())
                    return
                for i in range(start,n+1):
                    if i not in acc:
                        acc.append(i)
                        rec(acc,i +1 )
                        acc.pop()
            rec([],1)
            return ans