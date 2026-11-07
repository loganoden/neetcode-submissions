from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Time:
        # Space:

        num_rows = len(grid)
        num_cols = len(grid[0])

        if (grid[0][0] == 1
        or grid[num_rows - 1][num_cols - 1] == 1):
            return -1

        # Edge Case: [[0]]
        if num_rows == 1 and num_cols == 1:
            return 1

        shortest_path = 0
        queue = deque()

        # (Row, Col, Path Length)
        queue.append((0, 0, 1))
        grid[0][0] == 1
        
        while queue:
            r, c, path_len = queue.popleft()

            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (1, 1), (1, -1), (-1, 1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr == num_rows - 1 
                and nc == num_cols - 1):
                    return path_len + 1

                if (0 <= nr < num_rows
                and 0 <= nc < num_cols
                and grid[nr][nc] == 0):
                    grid[nr][nc] = 1
                    queue.append((nr, nc, path_len + 1))
                    
        return -1
