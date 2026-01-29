#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Reverse the graph: original u -> v becomes v -> u.
        # Node 0 being reachable from all nodes in the original graph is equivalent to
        # node 0 being able to reach all nodes in the reversed graph.
        rev_adj = [[] for _ in range(n)]
        max_possible_w = 0
        for u, v, w in edges:
            rev_adj[v].append((u, w))
            if w > max_possible_w:
                max_possible_w = w
        
        def can_reach_all(max_w: int) -> bool:
            visited = [False] * n
            visited[0] = True
            stack = [0]
            count = 1
            while stack:
                u = stack.pop()
                for v, w in rev_adj[u]:
                    if w <= max_w and not visited[v]:
                        visited[v] = True
                        count += 1
                        stack.append(v)
                        if count == n:
                            return True
            return count == n

        # Binary search on the range of possible weights
        low = 1
        high = max_possible_w
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach_all(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
# @lc code=end