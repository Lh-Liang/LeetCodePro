#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        from collections import deque
        
        if n == 1:
            return 0
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Count total nodes in each group (groups are 1-20)
        total_count = [0] * 21
        for g in group:
            total_count[g] += 1
        
        # BFS to find traversal order and parent relationships
        parent = [-1] * n
        order = []
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for child in adj[node]:
                if not visited[child]:
                    visited[child] = True
                    parent[child] = node
                    queue.append(child)
        
        # Process in reverse BFS order (leaf-to-root)
        result = 0
        subtree_count = [[0] * 21 for _ in range(n)]
        
        # Initialize: each node contributes 1 to its group count
        for i in range(n):
            subtree_count[i][group[i]] = 1
        
        for node in reversed(order):
            p = parent[node]
            if p != -1:
                # Add edge contribution for each group
                for g in range(1, 21):
                    cnt = subtree_count[node][g]
                    if cnt > 0:
                        result += cnt * (total_count[g] - cnt)
                # Merge into parent's subtree count
                for g in range(1, 21):
                    subtree_count[p][g] += subtree_count[node][g]
        
        return result
        
# @lc code=end