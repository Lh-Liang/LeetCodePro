#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict
        
        def dfs(node, parent, path_set):
            if nums[node] in path_set:
                return (0, float('inf'))
            
            path_set.add(nums[node])
            max_length = 0
            min_nodes = float('inf')
            
            for neighbor, length in graph[node]:
                if neighbor == parent:
                    continue
                
                l, n = dfs(neighbor, node, path_set)
                l += length
                if l > max_length:
                    max_length = l
                    min_nodes = n + 1
                elif l == max_length:
                    min_nodes = min(min_nodes, n + 1)
            
            path_set.remove(nums[node])
            return max_length, (min_nodes if max_length > 0 else 1)
        
        graph = defaultdict(list)
        for u, v, l in edges:
            graph[u].append((v, l))
            graph[v].append((u,l))															     	max_len , min_cnt = dfs(0 ,-1 ,set())   return [max_len ,min_cnt]   	# @lc code=end