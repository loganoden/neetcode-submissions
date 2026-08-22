class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        area = 0

        directions = {
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        }

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    stack = [(r, c)]
                    grid[r][c] = 0
                    area = 0

                    while stack:
                        row, col = stack.pop()
                        area += 1

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            # If we found land, then append tuple to stack
                            if (
                                nr >= 0 and nr < rows and
                                nc >= 0 and nc < cols and
                                grid[nr][nc] == 1
                            ):
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area