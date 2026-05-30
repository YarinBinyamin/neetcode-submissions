class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = 0
        while k > 0:
            ans = heapq.heappop(heap)
            k -= 1

        return -ans