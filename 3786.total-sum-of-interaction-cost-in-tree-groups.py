#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # We need to compute sum of distances between all pairs of nodes in the same group.
        # Since group values are limited to 1..20, we can process each group separately.
        # For each group, we need to compute sum of distances between all nodes in that group.
        # This can be done using tree DP: for each group, we consider the subtree containing only nodes of that group?
        # But groups are scattered. Alternative: use centroid decomposition or tree DP with contribution counting.
        # However, note constraints: n up to 1e5, groups up to 20 distinct values.
        # We can compute total distance sum for each group using rerooting DP on the whole tree,
        # but only considering nodes of that group.
        # Let's define for each node u and group g: count_g[u] = number of nodes in subtree of u (in rooted tree) that belong to group g.
        # And dist_g[u] = sum of distances from u to all nodes in subtree of u that belong to group g.
        # Then we can compute using DFS and then reroot to get for each node the total distance to all nodes in same group.
        # Then sum over all nodes (but each pair counted twice? Actually distance from u to v counted for both u and v?)
        # Better: For each group, we want sum_{u<v, same group} dist(u,v).
        # We can compute total distance sum for a group by using the formula:
        # sum_{u<v} dist(u,v) = (1/2) * sum_{u} sum_{v != u} dist(u,v).
        # So if we compute for each node u the total distance to all other nodes in same group, then sum over u and divide by 2.
        
        # Let's root the tree at 0 arbitrarily.
        # First DFS: compute subtree counts and distances for each group.
        K = max(group) + 1  # groups up to 20, but we can use dictionary or list size 21.
        cnt = [[0]*K for _ in range(n)]   # cnt[u][g] = number of nodes in subtree of u with group g
        dist = [[0]*K for _ in range(n)]  # dist[u][g] = sum of distances from u to those nodes in subtree
        
        parent = [-1]*n
        order = []
        stack = [0]
        parent[0] = -2  # mark visited
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        
        # Process in reverse order (post-order)
        for u in reversed(order):
            g_u = group[u]
            cnt[u][g_u] += 1   # node itself
            dist[u][g_u] += 0   # distance to itself is 0, but we don't need to add.
            for v in adj[u]:
                if v == parent[u]:
                    continue
                g_v = None
                for g in range(K):
                    if cnt[v][g]:
                        cnt[u][g] += cnt[v][g]
                        dist[u][g] += dist[v][g] + cnt[v][g]   # distance from u to nodes in v's subtree is increased by 1 edge (u-v)
            	# Actually we should iterate over all groups present. But K is at most 21, so okay."																					"	"}	"}	"}	"}	"}	"}	"}	"}	"}	"}	"}	"}	"}	"}"