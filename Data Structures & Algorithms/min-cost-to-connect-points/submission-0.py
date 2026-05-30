class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
            if not points:
                return 0
            total_cost = 0
            visited = set()
            points_keys = [(0, None, 0)] # (key, parent, index)

            while len(visited) < len(points):
                cost, parent, index = heapq.heappop(points_keys)
                if index in visited:
                    continue
                visited.add(index)
                total_cost += cost
                cur_x, cur_y = points[index]

                for i in range(len(points)):
                    if i not in visited:
                        x_i, y_i = points[i]
                        cur_dist = abs(cur_x - x_i) + abs(cur_y - y_i)
                        heapq.heappush(points_keys, (cur_dist, index, i))

            return total_cost
                
