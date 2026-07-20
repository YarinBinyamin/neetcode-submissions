"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        start_time = float('inf')
        end_time = float('-inf')
        for i in range(1,len(intervals)):
            start_time = max(intervals[i].start ,intervals[i-1].start)
            end_time = min(intervals[i].end ,intervals[i-1].end)
            if start_time < end_time:
                return False
        return True   