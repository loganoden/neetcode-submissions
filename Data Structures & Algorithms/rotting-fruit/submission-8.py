class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_mins = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(row, col):
            grid[row][col] = 0
            queue = [(row, col)]

            while queue:
                total_mins += 1
                r, c = queue.pop(0)

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 2:
                    bfs(r, c)

        return total_mins