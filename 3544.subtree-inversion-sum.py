#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Build tree structure using BFS from root
        children = [[] for _ in range(n)]
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        bfs_order = []
        
        while queue:
            node = queue.popleft()
            bfs_order.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    children[node].append(neighbor)
                    queue.append(neighbor)
        
        # Process in reverse BFS order (leaves first)
        process_order = bfs_order[::-1]
        
        # DP table: dp[node][d][flip]
        # d: distance to closest inverted ancestor (0 to k, k means can invert)
        # flip: 0 or 1 (parity of inversions from ancestors)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        
        for node in process_order:
            for d in range(k + 1):
                for flip in range(2):
                    sign = -1 if flip else 1
                    new_d = min(d + 1, k)
                    
                    # Option 1: Don't invert this node
                    result1 = sign * nums[node]
                    for child in children[node]:
                        result1 += dp[child][new_d][flip]
                    
                    # Option 2: Invert this node (only if d >= k)
                    if d >= k:
                        result2 = -sign * nums[node]
                        for child in children[node]:
                            result2 += dp[child][1][1 - flip]
                        dp[node][d][flip] = max(result1, result2)
                    else:
                        dp[node][d][flip] = result1
        
        return dp[0][k][0]
# @lc code=end