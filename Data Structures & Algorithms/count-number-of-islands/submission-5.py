class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(n * m), where n = num_rows and m = num_cols
        # Space: O(n * m)

        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def dfs(row, col):
            grid[row][col] = "0"
            stack = [(row, col)]

            while stack:
                row, col = stack.pop()

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < num_rows
                    and 0 <= nc < num_cols 
                    and grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))
            
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands