class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) +1
        for j in range(len(t)):
            dic[t[j]] = dic.get(t[j],0) -1
        for a in dic.values():
            if a != 0:
                return False
        return True