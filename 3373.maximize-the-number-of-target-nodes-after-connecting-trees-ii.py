#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        # Create adjacency list for both trees
        def build_adjacency_list(edges):
            adj_list = defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list
        
        adj1 = build_adjacency_list(edges1)
        adj2 = build_adjacency_list(edges2)
        
        def bfs_count_targets(start_node, adj):
            queue = deque([(start_node, 0)])  # node and level (distance from start_node) tuple
            seen = {start_node}
            count = 0
            while queue:
                node, level = queue.popleft()
                count += 1 if level % 2 == 0 else 0  # count as target if level is even
                for neighbor in adj[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, level + 1))
            return count
        
        n = len(adj1)  # number of nodes in first tree
m = len(adj2)  # number of nodes in second tree
result = []
f...