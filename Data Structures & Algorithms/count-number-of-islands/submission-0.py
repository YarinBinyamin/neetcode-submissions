class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        diretions = [[1,0], [-1,0], [0,-1],[0,1]]
        n = len(grid)
        m = len(grid[0])
        visited_graph = [[False for _ in range(m)] for _ in range(n)]
        components = 0 
        def dfs(i,j):
            visited_graph[i][j] = True
            for dr,dc in diretions:
                nr, nc = i + dr , j +dc
                if 0<=nr < n and 0<=nc<m and visited_graph[nr][nc] == False and grid[nr][nc] == '1':
                    dfs(nr,nc)
        for i in range(n):
            for j in range(m):
                if (visited_graph[i][j] == False) and grid[i][j] == '1':
                    components +=1
                    dfs(i,j)
        return components
            