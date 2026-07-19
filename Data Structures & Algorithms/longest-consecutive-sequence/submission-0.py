class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_map = set()
        for i in range(len(nums)):
            dict_map.add(nums[i])
        staring_points = set()
        for e in dict_map:
            if (e-1) not in dict_map:
                staring_points.add(e)
        max_len = 0
        cur_len = 1
        while staring_points:
            cur_start = staring_points.pop()
            while (cur_start+1) in dict_map:
                cur_len+=1
                cur_start+=1
            max_len = max(max_len,cur_len)
            cur_len =1
        return max_len
        