class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None for _ in range(len(word2))] for _ in range(len(word1))]
        
        def rec(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            elif j >= len(word2):
                return len(word1) - i

            elif i >= len(word1):
                return len(word2) - j
            if memo[i][j] is not None:
                return memo[i][j]
            if word1[i] == word2[j]:
                memo[i][j] = rec(i + 1, j + 1)
            else:
                insert = 1 + rec(i , j+1)
                delete = 1 + rec(i+1,j)
                replace = 1 + rec(i+1,j+1)
                memo[i][j] = min(insert,delete,replace)
            return memo[i][j]
        return rec(0,0)