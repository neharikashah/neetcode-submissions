class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxsize = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxsize = max(maxsize, self.dfs(row, col, rows, cols, grid))
                    

        
        return maxsize 

    def dfs(self, row, col, rows, cols, grid):
        if row<0 or col<0 or row>=rows or col>=cols or grid[row][col]!= 1:
            return 0

        grid[row][col] = 2
        
        return (1 + 
        self.dfs(row+1, col, rows, cols, grid) +
        self.dfs(row, col+1, rows, cols, grid) +
        self.dfs(row-1, col, rows, cols, grid) +
        self.dfs(row, col-1, rows, cols, grid))


        

        