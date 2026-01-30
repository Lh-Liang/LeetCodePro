#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def can_construct(max_weight):
            from collections import defaultdict, deque
            graph = defaultdict(list)
            for u, v, w in edges:
                if w <= max_weight:
                    graph[u].append((v, w))
            # Check if all nodes can reach node 0 with BFS/DFS
            visited = set()
            def bfs(start):
                queue = deque([start])
                visited.add(start)
                while queue:
                    node = queue.popleft()
                    for neighbor, _ in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            bfs(0)  # Start from node 0 to check reachability
            if len(visited) != n:
                return False  # Not all nodes can reach node 0
            # Ensure each node has at most 'threshold' outgoing connections with smaller weights prioritized.
            for u in range(n):
                if len(graph[u]) > threshold:
                    return False  # More than threshold connections from this node.
            return True
        # Binary search over possible max weights.
        low, high = min(w for _, _, w in edges), max(w for _, _, w in edges) + 1
        while low < high:
            mid = (low + high) // 2
            if can_construct(mid):
                high = mid  # Try smaller weights.
            else:
                low = mid + 1  # Increase weight to satisfy constraints. ​return -1 if low == max(w for _, _, w in edges) + 1 else low ​# @lc code=end