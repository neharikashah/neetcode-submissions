class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    q.append((row, col))
                    ans+=1
                    while q:
                        x, y = q.popleft()

                        if x > 0 and grid[x-1][y] == '1':
                            grid[x-1][y] = '0'
                            q.append((x-1, y))

                        if x < rows-1 and grid[x+1][y] == '1':
                            grid[x+1][y] = '0'
                            q.append((x+1, y))

                        if y > 0 and grid[x][y-1] == '1':
                            grid[x][y-1] = '0'
                            q.append((x, y-1))

                        if y < cols-1 and grid[x][y+1] == '1':
                            grid[x][y+1] = '0'
                            q.append((x, y+1))
        
        return ans



        