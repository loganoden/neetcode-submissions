class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-Source BFS
        
        rows = len(grid)
        cols = len(grid[0])

        # Use doubly-ended queue as BFS queue
        # Constant time add and remove from both sides
        rotten = deque()

        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                # Entry for each initial rotten fruit
                if grid[r][c] == 2:
                    rotten.append((r, c))
                # Keep track of number of fresh fruits
                elif grid[r][c] == 1:
                    fresh += 1
        
        # Infect each cell adjacent to rotten fruits
        # Continue running while the rotten deque isn't empty
        # Continue running while fresh fruits remain
        while rotten and fresh:
            # All infections within the minute
            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] != 1
                    ):
                        continue

                    # Infect fresh fruits
                    grid[nr][nc] = 2
                    rotten.append((nr, nc))
                    fresh -= 1

            minutes += 1

        return -1 if fresh else minutes