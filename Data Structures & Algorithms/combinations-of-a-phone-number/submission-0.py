class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        my_dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ans = []
        def rec(i, cur :str):
            if i == len(digits):
                ans.append("".join(cur))
                return 
            if i > len(digits):
                return
            for d in my_dict[digits[i]]:
                cur.append(d)
                rec(i+1,cur)
                cur.pop()
        rec(0,[])
        return ans