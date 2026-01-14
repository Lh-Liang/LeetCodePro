#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#
# @lc code=start
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_parity_info(edges, n):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            parity = [-1] * n
            parity[0] = 0
            count = [0, 0]
            queue = deque([0])
            
            while queue:
                node = queue.popleft()
                count[parity[node]] += 1
                for neighbor in graph[node]:
                    if parity[neighbor] == -1:
                        parity[neighbor] = 1 - parity[node]
                        queue.append(neighbor)
            
            return parity, count
        
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        parity1, count1 = get_parity_info(edges1, n)
        _, count2 = get_parity_info(edges2, m)
        
        max_from_tree2 = max(count2)
        
        return [count1[parity1[i]] + max_from_tree2 for i in range(n)]
# @lc code=end