class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        n = len(board)
        m = len(board[0])
        
        queue = deque()
        
        for i in range(n):
            for j in range(m):
                    if ((i == 0 or i == n - 1 or j == 0 or j == m - 1)
                        and board[i][j] == "O"):
                        queue.append((i, j))
                        board[i][j] = "S"
        
        operations = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            cur_i, cur_j = queue.popleft()
            for di, dj in operations:
                new_i = cur_i + di
                new_j = cur_j + dj

                if (0 <= new_i < n and 0 <= new_j < m and board[new_i][new_j] == "O"):
                    board[new_i][new_j] = "S"
                    queue.append((new_i, new_j))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"     
        