#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        # Build adjacency list for graph representation of method invocations
        adj_list = defaultdict(list)
        reverse_adj_list = defaultdict(list)
        for ai, bi in invocations:
            adj_list[ai].append(bi)
            reverse_adj_list[bi].append(ai)
        
        # Collect all reachable nodes from k (suspicious nodes) using DFS
        def collect_suspicious(start):
            stack = [start]
            visited = set()
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(adj_list[node])
            return visited
        
        suspicious_methods = collect_suspicious(k)
        # Check for external invocation to suspicious nodes
        for sm in suspicious_methods:
            if any(invoker not in suspicious_methods for invoker in reverse_adj_list[sm]):
                return list(range(n))  # Return all methods because we can't remove them cleanly.
        
        # Return non-suspicious methods only if possible to remove all suspicious ones.
        return [i for i in range(n) if i not in suspicious_methods]
# @lc code=end