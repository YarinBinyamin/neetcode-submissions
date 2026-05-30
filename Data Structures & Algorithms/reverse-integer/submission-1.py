class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        sum = 0
        if x < 0 :
            sign = -1
        x_converted = str(abs(x))
        pow = 1
        for ch in x_converted:
            sum += int(ch)*pow
            pow *=10
        sum =sum*sign
        if sum < -2**31 or sum > 2**31 -1:
            return 0
        return sum 