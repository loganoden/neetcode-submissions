class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Once we discover a grid, immediately mark it as water ("0")
        # Make sure to explore an entire island first before moving on

        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def dfs(row, col):
            grid[row][col] = "0"
            if row > 0 and grid[row - 1][col] == "1":
                dfs(row - 1, col)
            if row < num_rows-1 and grid[row + 1][col] == "1":
                dfs(row + 1, col)
            if col > 0 and grid[row][col - 1] == "1":
                dfs(row, col - 1)
            if col < num_cols-1 and grid[row][col + 1] == "1":
                dfs(row, col + 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands
        
            
