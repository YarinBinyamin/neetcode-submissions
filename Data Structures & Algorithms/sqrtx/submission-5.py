class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        if x==1:
            return 1
        stop_con = x//2
        ans=0
        for i in range(stop_con+1):
            if i*i == x:
                return i
            if i*i > x:
                break
            ans = i
        return ans