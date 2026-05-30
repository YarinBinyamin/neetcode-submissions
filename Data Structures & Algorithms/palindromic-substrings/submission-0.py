class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        
        def CheckEven(i): 
            pali = 0
            left,right = i, (i+1)
            while 0<=left and right < len(s):
                if not (s[left] == s[right]):
                    break
                pali +=1
                left -=1
                right +=1
            return pali
        def CheckOdd(i):
            pali = 0 
            left, right= i,i
            while 0<=left and right < len(s):
                if not (s[left] == s[right]):
                    break
                pali +=1
                left -=1
                right +=1
            return pali
        for i in range(len(s)):
            total+= CheckEven(i) +CheckOdd(i)
        return total 