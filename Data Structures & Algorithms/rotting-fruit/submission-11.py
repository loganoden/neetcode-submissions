from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time:
        # Space:
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        queue = deque()
        fresh = 0
        total_minutes = 0

        # Account for all current rotting oranges at same time
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            current_minute = len(queue)

            for _ in range(current_minute):
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
            total_minutes += 1

        return total_minutes if fresh == 0 else -1

