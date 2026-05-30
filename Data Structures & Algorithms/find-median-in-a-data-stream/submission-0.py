class MedianFinder:

    def __init__(self):
        self.right_heap = [] # save positive so get min is easy [0]
        self.left_heap = [] # save negative so we get max here 
        self.counter = 0
        
            
    def addNum(self, num: int) -> None:
            self.counter +=1
            if  len(self.left_heap) == 0 or num <= -self.left_heap[0]:
                heapq.heappush(self.left_heap, -num)
            else:
                heapq.heappush(self.right_heap, num)
            if len(self.left_heap) > len(self.right_heap) + 1:
                heapq.heappush(self.right_heap,  -heapq.heappop(self.left_heap))
            elif len(self.right_heap) > len(self.left_heap):
                heapq.heappush(self.left_heap,  -heapq.heappop(self.right_heap))
                
        

    def findMedian(self) -> float:
        if self.counter % 2 == 0 :
            return ((-self.left_heap[0]) + self.right_heap[0]) / 2
        else :
            return  (-self.left_heap[0])
        