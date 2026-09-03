class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        seen = set()
        maxArea = 0

        def bfs(r, c):
            q = []
            q.append((r, c))
            seen.add((r, c))
            lands = 1

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == 1
                        and (r, c) not in seen
                    ):
                        q.append((r, c))
                        seen.add((r, c))
                        lands += 1
                
            return lands
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] not in seen and grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea
