#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        from collections import defaultdict, deque
        if not edges:
            return -1 if n > 1 else 0
        # Collect all unique weights
        weights = sorted(set(w for _, _, w in edges))
        left, right = 0, len(weights) - 1
        answer = -1
        # Build original edge list for fast filtering
        edge_list = [[] for _ in range(n)]
        for u, v, w in edges:
            edge_list[u].append((v, w))
        def feasible(maxW):
            # Build subgraph with edge weight <= maxW
            adj = [[] for _ in range(n)]
            out_deg = [0] * n
            in_rev = [[] for _ in range(n)]
            for u in range(n):
                for v, w in edge_list[u]:
                    if w <= maxW:
                        adj[u].append(v)
                        out_deg[u] += 1
                        in_rev[v].append(u)
            # Out-degree check
            if any(d > threshold for d in out_deg):
                return False
            # Check reachability: all nodes must reach node 0 (i.e., from every node there is a path to 0)
            # We do this by BFS/DFS from 0 in the reversed graph
            seen = [False] * n
            stack = [0]
            seen[0] = True
            while stack:
                u = stack.pop()
                for v in in_rev[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
            return all(seen)
        # Binary search on weights
        while left <= right:
            mid = (left + right) // 2
            maxW = weights[mid]
            if feasible(maxW):
                answer = maxW
                right = mid - 1
            else:
                left = mid + 1
        return answer
# @lc code=end