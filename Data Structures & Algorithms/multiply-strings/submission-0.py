class Solution:
    def multiply(self, num1: str, num2: str) -> str:
            def convetToInt(num : str) -> int:
                ans = 0 
                pow = 1
                for i in range(len(num) -1 , -1 , -1):
                    val = int(num[i]) * pow
                    ans += val
                    pow*=10
                return ans
            num1_int = convetToInt(num1)
            num2_int = convetToInt(num2)
            return str(num1_int * num2_int)