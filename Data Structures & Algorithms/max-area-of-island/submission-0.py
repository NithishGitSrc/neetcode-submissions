class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = [[0]*COLS for _ in range(ROWS)]
        maxIslandArea = 0

        def bfs(r,c):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c]==0 or
                visit[r][c]==1):
                return 0
            
            visit[r][c] = 1

            return 1 + ( bfs(r+1,c) +
            bfs(r-1,c) + 
            bfs(r,c+1) + 
            bfs(r,c-1) )


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and visit[r][c] == 0:
                    area = bfs(r,c)
                    maxIslandArea = max( area, maxIslandArea)

        return maxIslandArea
        