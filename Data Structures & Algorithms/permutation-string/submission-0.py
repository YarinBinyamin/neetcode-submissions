class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqs1 = [0] *26
        freqs2 = [0] *26
        for i in range(len(s1)):
            freqs1[ord(s1[i])- ord('a')] +=1
            freqs2[ord(s2[i])- ord('a')] +=1
        l,r = 0 , len(s1)
        while r < len(s2):
            if freqs1 == freqs2:
                return True
            freqs2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            freqs2[ord(s2[r]) - ord('a')] += 1
            r += 1
        return freqs1 == freqs2
