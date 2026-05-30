class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None for _ in range(len(s))]
        def rec(i) :
            if i == len(s):
                return True
            if memo[i] is not None:
                return memo[i]
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if rec(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return rec(0)
            