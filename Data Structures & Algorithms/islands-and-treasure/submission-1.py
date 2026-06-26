class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        COL, ROW = len(grid[0]), len(grid)
        q = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            row, col = q.popleft()
            coordinates = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in coordinates:
                r, c = row + dr, col + dc
                if (r < 0 or c < 0 or COL <= c or ROW <= r or grid[r][c] != 2147483647):
                    continue
                q.append((r, c))
                grid[r][c] = grid[row][col] + 1 
        

        