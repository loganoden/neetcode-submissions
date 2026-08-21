class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time:  O(rows * cols)
        # Space: O(rows * cols) worst case from the DFS recursion stack

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(r, c):
            # Return if outside grid or found already explored land/water
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return

            # Mark current cell as explored
            grid[r][c] = "0"

            # Run DFS on the 4 adjacent cells
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
            
            