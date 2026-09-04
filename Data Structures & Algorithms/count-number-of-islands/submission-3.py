"""
For each row and col, you go through everything, you want to return the number of islands.

Once you reach one 1, you run a bfs or a dfs on it to grab all the indexes that you already have visited.

Then, you add 1 to the number of islands.

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                    ):
                        q.append((r, c))
                        grid[r][c] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1

        return numIslands
