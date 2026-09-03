"""
We want to go through the rows and find the place where it equals to 1. Then, we can do a graph traversal (bfs) on that 1 to find all the other adjacent "lands". Then, we put all those into a set called seen so we don't call bfs on them again.


"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def bfs(r, c):

            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))
            
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in seen
                    ):
                        seen.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1

        return islands
