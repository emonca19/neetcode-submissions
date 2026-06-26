class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        COL, ROW = len(grid[0]), len(grid)
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            dimension = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dimension:
                row, col = r + dr, c + dc
                if (row < 0 or col < 0 or ROW <= row or COL <= col or grid[row][col] != 2147483647):
                    continue
                
                grid[row][col] = 1 + grid[r][c]
                q.append((row, col))
        