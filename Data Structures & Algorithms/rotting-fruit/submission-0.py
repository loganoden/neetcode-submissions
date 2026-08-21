class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-Source BFS
        
        rows = len(grid)
        cols = len(grid[0])

        # Use doubly-ended queue as BFS queue
        # Constant time add and remove from both sides
        rotten = deque()
        temp = deque()

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

        # BFS
        def bfs(r, c):
            nonlocal fresh
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return

            # Infect fresh fruits
            if grid[r][c] == 1:
                grid[r][c] = 2
                temp.append((r, c))
                fresh -= 1
        
        # Run BFS on each cell adjacent to rotten fruits
        # Continue running until the rotten deque is empty
        while rotten:
            r, c = rotten.pop()
            bfs(r-1, c)
            bfs(r+1, c)
            bfs(r, c-1)
            bfs(r, c+1)
            if not rotten and temp:
                if temp:
                    minutes += 1
                    rotten.extend(temp)
                    temp.clear()


        return -1 if fresh else minutes
