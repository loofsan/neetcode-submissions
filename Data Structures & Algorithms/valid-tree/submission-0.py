class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS
        visited = set()
        queue = deque([0])
        visited.add(0)

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append(neighbor)

        # Every node must be reachable from 0
        return len(visited) == n