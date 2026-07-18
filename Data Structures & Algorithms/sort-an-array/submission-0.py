class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(right_arr, left_arr):
            sorted_array = []
            i=j=0
            
            while i < len(right_arr) and j < len(left_arr):
                if right_arr[i] <= left_arr[j]:
                    sorted_array.append(right_arr[i])
                    i+=1
                else:
                    sorted_array.append(left_arr[j])
                    j+=1
            while i < len(right_arr):
                sorted_array.append(right_arr[i])
                i+=1
            while j < len(left_arr):
                sorted_array.append(left_arr[j])
                j+=1
            return sorted_array
        def merge_srt(arr):
            if len(arr) <=1:
                return arr
            mid = len(arr)//2
            right_arr =merge_srt(arr[:mid])
            left_arr = merge_srt(arr[mid:])
            
            return merge( right_arr, left_arr)

        return merge_srt(nums)
        
            
