class Solution:
    def dfs(self, i, j , grid, m, n):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '1':
            return

        grid[i][j] = '*'

        self.dfs(i + 1, j, grid, m, n)
        self.dfs(i - 1, j, grid, m, n)
        self.dfs(i, j + 1, grid, m, n)
        self.dfs(i, j - 1, grid, m, n)








    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count+=1
                    self.dfs(i, j , grid, m, n)

        return count