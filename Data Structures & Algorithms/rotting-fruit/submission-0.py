class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , column = len(grid), len(grid[0])
        q= collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(column):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] ==1 :
                    fresh +=1
        if fresh == 0:
            return 0
        
        mintues =0 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    
                    if 0 <= nr < rows and 0 <= nc < column and grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        fresh -=1
                        q.append((nr,nc))
            mintues +=1
        
        return mintues if fresh == 0 else -1  