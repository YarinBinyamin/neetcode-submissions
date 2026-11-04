class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            new_target = target - nums[i]
            for nail in range(i+1,len(nums)-2):
                if nail > i + 1 and nums[nail] == nums[nail - 1]:
                    continue
                nailed_new_target = new_target - nums[nail]
                left,right = nail+1, len(nums)-1
                
                while left<right:
                    if nailed_new_target == nums[right] + nums[left]:
                        ans.append([nums[i],nums[nail],nums[left],nums[right]])
                        left +=1
                        right -=1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nailed_new_target > nums[right] + nums[left] :
                        left+=1
                    else :
                        right-=1
        return ans