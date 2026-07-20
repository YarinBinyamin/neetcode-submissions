class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x ==0: return 0.0
        if n == 0: return 1.0
        
        ans = float(1)
        if n < 0:
            x= float(1/x)
            n=-n
        while n > 0:
            if n % 2 == 1:
                ans *=x
            x *=x
            n //=2

        return ans