class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = set()
        ops = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(cur_trie, row , col):
            if ((row,col) in visited):
                return
            visited.add((row,col))
            if cur_trie is None:
                return
            if "#" in cur_trie:
                ans.add(cur_trie["#"])
            for op in ops:
                new_row, new_col = row + op[0] , col + op[1]
                if 0<=new_row <n and 0<=new_col <m :
                    ch = board[new_row][ col + op[1]]
                    if ch in cur_trie:
                        dfs(cur_trie[ch], new_row ,  col + op[1])
            visited.remove((row, col))
        trie = {}
        for word in words:
            cur = trie
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['#'] = word
        n = len(board)
        m = len(board[0])
        cur = trie
        for i in range(n):
            for j in range(m):
                ch = board[i][j]
                if ch in cur:
                    visited = set()
                    dfs(cur[ch], i, j )
        return list(ans)
                    