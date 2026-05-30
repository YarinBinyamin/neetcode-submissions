class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPali(word):
            l,r = 0 , len(word) -1
            while l <= r :
                if word[l] != word[r]:
                    return False
                l +=1
                r -=1
            return True
        def rec(start,acc):
            if start == len(s):
                ans.append(acc.copy())
                return
            for i in range(start,len(s)):
                if isPali(s[start:i+1]):
                    acc.append(s[start:i+1])
                    rec(i+1,acc)
                    acc.pop()
            return ans
        return rec(0,[])
