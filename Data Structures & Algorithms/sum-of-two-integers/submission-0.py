class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a_binary = [int(c) for c in format(a & mask, "032b")]
        b_binary = [int(c) for c in format(b & mask, "032b")]
        ans = []
        carry = 0
        for i in range(31, -1, -1):
            a_i = a_binary[i]
            b_i = b_binary[i]
            bit = carry ^ a_i ^ b_i
            ans.insert(0, bit)
            carry = 1 if a_i + b_i + carry >= 2 else 0
        result = int("".join(map(str, ans)), 2)
        if result <= 0x7fffffff:
            return result
        else:
            return result - 0x100000000