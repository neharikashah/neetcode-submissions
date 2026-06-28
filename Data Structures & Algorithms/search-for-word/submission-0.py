class Solution:
    
    


    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        n = len(board)
        m = len(board[0])

        wl = len(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(word, board, i , j, 0, n, m):
                        return True

        return res


    def dfs(self, word, board, x, y, k, n, m):
        wl = len(word)
        
        if x < 0 or x >= n or y < 0 or y >=m  or word[k] != board[x][y]:
             return False
        
        if k == wl-1:
            return True

        c = board[x][y]
        board[x][y] = '*'
        nextt = self.dfs(word, board, x-1 , y, k+1, n, m) or self.dfs(word, board, x+1 , y, k+1, n, m) or self.dfs(word, board, x , y-1, k+1, n, m) or self.dfs(word, board, x , y+1, k+1, n, m)
        board[x][y] = c

        return nextt

            