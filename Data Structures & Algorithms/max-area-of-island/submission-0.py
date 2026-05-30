class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        land = set()
        cal = [(1,0),(-1,0),(0,1),(0,-1)]
        n= len(grid)
        m= len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land.add((i,j))
        maxLand = 0
        queue = []
        while land:
            curLand = 0 
            cell = land.pop()
            queue.append(cell)
            while queue:
                row, col  = cell
                curLand +=1
                for e in cal:
                    if (row+e[0], col+e[1]) in land:
                        land.remove((row+e[0], col+e[1]))
                        queue.append((row+e[0], col+e[1]))                   
                cell = queue.pop()
            maxLand=max(curLand,maxLand)
            curLand = 0
        return maxLand       