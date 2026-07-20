class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        ans = ""
        index1 = 0
        index2 = 0
        while index1 < min_len and index2 < min_len:
            ans += word1[index1]
            ans += word2[index2]
            
            index1+=1
            index2+=1
        if index1 < len(word1):
            ans += word1[index1:]
        elif index2 < len(word2):
            ans += word2[index2:]
        return ans            
            