"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
                rooms = []
                intervals.sort(key=lambda iv: iv.start) ##
                for cur in intervals:
                    falg = False
                    for i in range(len(rooms)):
                        if rooms[i] <= cur.start:
                            rooms[i] = cur.end
                            falg = True
                            break
                    if not falg:
                        rooms.append(cur.end)
                            
                return len(rooms)