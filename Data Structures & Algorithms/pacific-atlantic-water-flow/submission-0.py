class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ops = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific = set()
        atlantic = set()
        n = len(heights)
        m = len(heights[0])
        for i in range(m):
            pacific.add((0, i))
            atlantic.add((n-1, i))
        for i in range(n):
            pacific.add((i, 0))
            atlantic.add((i, m-1))
        def dfs(starts):
            visited = set()
            line = list(starts)
            while line:
                a, b = line.pop()
                if (a, b) in visited:
                    continue
                visited.add((a, b))
                for c, d in ops:
                    _x, _y = a + c, b + d
                    if (0 <= _x < n and 0 <= _y < m and
                        (_x, _y) not in visited and
                        heights[_x][_y] >= heights[a][b]):

                            line.append((_x, _y))

            return visited

        pacific_reachable = dfs(pacific)
        atlantic_reachable = dfs(atlantic)

        return [list(cell) for cell in pacific_reachable & atlantic_reachable]