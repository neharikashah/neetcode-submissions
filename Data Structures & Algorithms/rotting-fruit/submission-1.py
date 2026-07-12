class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        mintime = 0
        q = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh +=1

        if fresh == 0:
            return 0
                    
        while q and fresh> 0:

            size = len(q)
            mintime +=1
            for _ in range(size):
                x, y = q.popleft()

                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    fresh -=1 
                    q.append((x-1, y))

                if x < rows-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    fresh -=1 
                    q.append((x+1, y))

                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    fresh -=1 
                    q.append((x, y-1))

                if y < cols-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    fresh -=1 
                    q.append((x, y+1))

        if fresh == 0:
            return mintime
        else:
            return -1 



        

        