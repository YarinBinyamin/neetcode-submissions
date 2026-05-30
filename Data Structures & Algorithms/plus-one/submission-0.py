class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = []
        pos = 1
        total = 0
        for i in range(n-1,-1,-1):
            num = digits[i]
            total += (num *pos)
            pos *=10
        total+=1
        while total != 0 :
            to_add =total %10
            total = total //10
            ans.append(to_add)
        return ans[::-1]