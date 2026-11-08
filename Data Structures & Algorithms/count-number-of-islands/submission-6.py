class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def dfs(row, col): 
            grid[row][col] = "0"
            stack = [(row, col)]

            while stack:
                r, c = stack.pop()
                for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)

        return num_islands