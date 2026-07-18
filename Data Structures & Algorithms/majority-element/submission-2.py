class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            candidate =0 
            count =1 
            for e in nums:
                if e == candidate:
                    count +=1
                else:
                    count -=1
                if count ==0 :
                    candidate = e
                    count =1 
            return candidate