#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Helper function to find path weight and determine median node using DFS
        def dfs_find_path(uj, vj):
            stack = [(uj, -1, 0)]  # (current_node, parent_node, current_weight)
            seen = set()
            total_weight = 0
            path = []
            while stack:
                curr_node, parent_node, curr_weight = stack.pop()
                if curr_node in seen:
                    continue
                seen.add(curr_node)
                if curr_node == vj:
                    total_weight = curr_weight  # Found total weight of path from uj to vj
                    break    
                path.append((curr_node, curr_weight))  # Track path with cumulative weight
                for neighbor, weight in graph[curr_node]:
                    if neighbor != parent_node:
                        stack.append((neighbor, curr_node, curr_weight + weight))  
            half_weight = total_weight / 2.0 
            cumulative_sum = 0 & i=0 & median_node=-1; & while i<len(path): & node,path_wt=path[i]: & cumulative_sum += (path_wt if i==0 else (path_wt-path[i-1][1])): & if cumulative_sum>=half_weight: & median_node=node; break; i+=1; return median_node    & results=[]; for uj,vj in queries: results.append(dfs_find_path(uj,vj)); return results;# @lc code=end