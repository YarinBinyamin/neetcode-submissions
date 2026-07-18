class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n ==0 :
            return 
        k%=n
        moved = 0 
        start =0 

        carry = nums[start]
        start = 0
        while moved < n:
            current_index = start
            carry = nums[start]
            while True:
                next_index = (current_index + k) % n

                displaced = nums[next_index]
                nums[next_index] = carry
                carry = displaced
                current_index = next_index
                moved+=1 

                if current_index == start:
                    break
            start +=1
        return nums
        