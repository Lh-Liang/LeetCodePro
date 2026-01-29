#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict

        MOD = 10**9 + 7
        # Construct adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def find_path(u, v):
            # BFS to find path from u to v
            parent = {u: None}
            stack = [u]
            while stack:
                node = stack.pop()
                if node == v:
                    break
                for neighbor in tree[node]:
                    if neighbor not in parent:
                        parent[neighbor] = node
                        stack.append(neighbor)
            
            # Reconstruct path from u to v using parent map
            path = []
            step = v
            while step is not None:
                path.append(step)
                step = parent[step]
            return path[::-1]
        
        def count_odd_assignments(path_length):
            if path_length % 2 == 0:
                return (2 ** (path_length - 1)) % MOD # Half of combinations lead to odd cost when even length
            else:
                return (2 ** (path_length - 1)) % MOD # Half when odd length also leads to odd cost due to parity change
        
        results = []
        for u, v in queries:
            path = find_path(u, v)
            num_edges = len(path) - 1
            valid_assignments = count_odd_assignments(num_edges)
            results.append(valid_assignments)
        
        return results
# @lc code=end