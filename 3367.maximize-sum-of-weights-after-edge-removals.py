#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        from collections import defaultdict
        import heapq
        n = len(edges) + 1
        adj = defaultdict(list)
        edge_ids = {}
        total = 0
        # Build adjacency list and track edge indices
        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((w, v, idx))
            adj[v].append((w, u, idx))
            edge_ids[(min(u,v), max(u,v))] = idx
            total += w
        removed = set()
        # For each node, if its degree > k, remove smallest-weight edges
        for node in range(n):
            if len(adj[node]) > k:
                # sort by weight
                adj[node].sort()
                # Remove len(adj[node]) - k smallest edges for this node
                to_remove = len(adj[node]) - k
                for i in range(to_remove):
                    w, neighbor, idx = adj[node][i]
                    # Remove only if not already removed
                    eid = (min(node, neighbor), max(node, neighbor))
                    if eid not in removed:
                        removed.add(eid)
                        total -= w
        return total
# @lc code=end