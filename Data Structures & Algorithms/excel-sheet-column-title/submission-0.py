class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1 
            remainder = columnNumber % 26
            ans.append(chr(remainder + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(ans))