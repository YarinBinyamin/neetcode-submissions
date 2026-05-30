class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
            intervals.sort(key=lambda x: x[0])

            sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))

            ans = [-1] * len(queries)
            heap = []
            i = 0

            for q, original_idx in sorted_queries:

                # Add all intervals whose left <= q
                while i < len(intervals) and intervals[i][0] <= q:
                    left, right = intervals[i]
                    length = right - left + 1
                    heapq.heappush(heap, (length, right))
                    i += 1

                # Remove intervals that ended before q
                while heap and heap[0][1] < q:
                    heapq.heappop(heap)

                # Smallest valid interval is now on top
                if heap:
                    ans[original_idx] = heap[0][0]

            return ans