class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        max_len = 0
        start = 0
        i =0
        while i < len(s):
            if s[i] in found:
                    while s[i] in found:
                        found.remove(s[start])
                        start += 1
                    found.add(s[i])
                    max_len = max(max_len, i - start + 1)
            else:
                found.add(s[i])
            max_len = max(max_len,i - start + 1)
            i+=1
        return max_len