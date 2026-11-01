from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        total_mins = 0
        fresh = 0
        queue = deque()

        # Find every starting source and count fresh oranges
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            # Process only oranges in this minute's layer
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            total_mins += 1
        
        return total_mins if fresh == 0 else -1