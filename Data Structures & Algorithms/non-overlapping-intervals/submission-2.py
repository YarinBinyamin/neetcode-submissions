class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removal_items = 0
        cur_start,cur_end = intervals[0][0],intervals[0][1]
        index = 1
        while index < len(intervals):
            if not (max(cur_start,intervals[index][0]) < min(cur_end,intervals[index][1])):
                cur_start = max(cur_start,intervals[index][0])
                cur_end = max(cur_end,intervals[index][1])
                index +=1
                continue
            else:
                cur_start = max(cur_start,intervals[index][0])
                cur_end = min(cur_end,intervals[index][1])
                index +=1
                removal_items+=1
        return  removal_items