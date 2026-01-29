# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        from collections import defaultdict, deque
        
        # Build adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Union-Find data structure to manage connected components within same group
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        # Connect nodes within the same group using union-find
        for u, v in edges:
            if group[u] == group[v]:
                union(u, v)
        
        # Calculate interaction costs within each component of a group
        total_interaction_cost = 0
        seen_components = set()

        # Function to calculate distances using BFS
        def bfs(start_node):
            queue = deque([(start_node, 0)])
            visited = set([start_node])
            total_cost = 0
            while queue:
                node, dist = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited and group[neighbor] == group[start_node]:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
                        total_cost += dist + 1 # Add distance to total cost for this edge path
            return total_cost

        # Iterate through each node and calculate cost for its component if not processed
        for i in range(n):
            component_root = find(i)
            if (group[i], component_root) not in seen_components:
                seen_components.add((group[i], component_root))
                # Calculate cost for this component starting from any node like i belonging to it
                total_interaction_cost += bfs(i)
                
        return total_interaction_cost // 2 # Each pair counted twice so divide by 2
# @lc code=end