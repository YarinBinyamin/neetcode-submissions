class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        s = set()
        heap = []

        edges = [[] for _ in range(n + 1)]
        dist = [float("inf")] * (n + 1)
        for edge in times:
            edges[edge[0]].append([edge[1],edge[2]])
        heap = [(0, k)]
        dist[k] = 0
        while heap:
            u_time,u_i = heapq.heappop(heap)
            if u_i in s:
                continue
            s.add(u_i)
            for nei in edges[u_i]:
                v_i,v_time = nei
                if v_i not in s:
                    if dist[v_i] > u_time + v_time:
                        dist[v_i] = u_time + v_time
                        heapq.heappush(heap, (dist[v_i], v_i))
        ans = max(dist[1:])
        return ans if ans != float("inf") else -1