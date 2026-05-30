class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        def CheckEven(i):
            left,right = i, (i+1)
            while 0<=left and right < len(s):
                if not (s[left] == s[right]):
                    break
                left -=1
                right +=1
            return s[left +1 : right ]
        def CheckOdd(i):
            left, right= i,i
            while 0<=left and right < len(s):
                if not (s[left] == s[right]):
                    break
                left -=1
                right +=1
            return s[left +1: right ]
        for i in range(len(s)):
            c = CheckEven(i)
            if len(c) > len(max_pal):
                max_pal = c
            d = CheckOdd(i)
            if len(d) > len(max_pal):
                    max_pal = d
        return max_pal