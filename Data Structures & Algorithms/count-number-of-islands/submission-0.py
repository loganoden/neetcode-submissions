class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(r, c):
            # Return if got outside grid or found already explored land or water
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return

            # Mark current grid as explored
            grid[r][c] == "0"

            # Run dfs on the 4 adjacent grids
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
            
            