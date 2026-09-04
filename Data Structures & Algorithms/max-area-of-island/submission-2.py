class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        seen = set()

        def bfs(r, c):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q = collections.deque()
            q.append((r, c))
            seen.add((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == 1
                        and (r, c) not in seen
                    ):
                        q.append((r, c))
                        area += 1
                        seen.add((r, c))

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    islandArea = bfs(r, c)
                    maxArea = max(maxArea, islandArea)

        return maxArea
