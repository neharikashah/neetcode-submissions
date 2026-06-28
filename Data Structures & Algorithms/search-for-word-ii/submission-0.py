class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

    def addword(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isend = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])

        root = TrieNode()
        for w in words:
            root.addword(w)

        res = set()

        def dfs(i, j, root, curword):
            if i<0 or j<0 or i>=n or j>=m or board[i][j] not in root.children:
                return
            
            root = root.children[board[i][j]]
            curword += board[i][j]

            if root.isend:
                res.add(curword)
            
            temp = board[i][j]
            board[i][j] = '*'

            dfs(i-1, j, root, curword)
            dfs(i, j-1, root, curword)
            dfs(i+1, j, root, curword)
            dfs(i, j+1, root, curword)

            board[i][j] = temp


        
        for i in range(n):
            for j in range(m):
                dfs(i, j, root, "")

        return list(res)


        
            

        