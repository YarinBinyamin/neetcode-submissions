class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        n = len(intervals)
        i = 0 
        # skip all intervasls that completley bewfore our new interval
        while i < n and intervals[i][1] < new_start:
            i+=1
        start_index = i
        #here is my position - but might merge with others
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start,intervals[i][0])
            new_end = max(new_end,intervals[i][1])
            i+=1
        intervals[start_index:i] = [[new_start,new_end]]
        return intervals 