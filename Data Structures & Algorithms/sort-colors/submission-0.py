class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i1,i2):
            temp= nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp
        n = len(nums)
        l,r = 0 , n-1
        cur = 0
        while cur <= r:
            if nums[cur] == 0:
                swap(l,cur)
                l+=1
                cur+=1
            elif nums[cur] ==2 :
                swap(r,cur)
                r-=1
            else:
                cur+=1