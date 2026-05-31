class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(open,close, acc):
            if close > open and close == 0:
                return
            if close == 0 and open ==0:
                cur = "".join(acc)
                if cur not in ans:
                    ans.append(cur)
                return
            if open<close and open >=0:
                acc.append(')')
                rec(open,close-1,acc)
                acc.pop()
            if open >0:
                acc.append('(')
                rec(open-1,close,acc)            
                acc.pop()
        rec(n,n,[])  
        return ans 