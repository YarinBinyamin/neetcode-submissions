class TimeMap:

        def __init__(self):
                self.last_timestamp = 0 
                self.my_map: dict[str, list[tuple[int, str]]] = {}   

        def set(self, key: str, value: str, timestamp: int) -> None:
                if timestamp < self.last_timestamp:
                        return 
                if key not in self.my_map:
                        self.my_map[key] = []
                self.my_map[key].append((timestamp, value))
                self.last_timestamp = timestamp  

        def binarySearch(self, time : int  , arr ):
                left, right = 0 , len(arr) - 1 
                ans = ""
                while left <= right : 
                        mid = left + (right - left) // 2
                        cur_time, cur_val = arr[mid]
                        if cur_time == time:
                                ans = cur_val
                                return ans
                        elif cur_time < time:
                                left = mid +1
                                ans = cur_val
                        else:
                                right = mid -1
                return ans                           

        def get(self, key: str, timestamp: int) -> str:
                if  key not in self.my_map :
                        return ""
                answer =  self.binarySearch(timestamp, self.my_map[key])
                print(answer)
                return answer                               
