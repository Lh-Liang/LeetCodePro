#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#
from typing import List, Dict
from collections import defaultdict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # Step 2: Build graph as adjacency list
        graph = defaultdict(list)
        for u, v, l in edges:
            graph[u].append((v, l))
            graph[v].append((u, l))
        
        # Helper function for DFS traversal with backtracking
        def dfs(node: int, parent: int, visited_values: set) -> (int, int):
            max_length = 0
            min_nodes = float('inf')
            visited_values.add(nums[node])
            
            for neighbor, length in graph[node]:
                if neighbor == parent:
                    continue
                if nums[neighbor] in visited_values:
                    continue
                
                path_length, num_nodes = dfs(neighbor, node, visited_values)
                total_length = path_length + length
                
                if total_length > max_length:
                    max_length = total_length
                    min_nodes = num_nodes + 1
                elif total_length == max_length:
                    min_nodes = min(min_nodes, num_nodes + 1)
            
            visited_values.remove(nums[node])
            return max_length if max_length > 0 else 0, min_nodes if max_length > 0 else 1 # Correct handling for zero-length paths.
        
        # Step 7 & Step 8: Calculate overall maximum special path from any starting node efficiently using tree properties if possible.
        overall_max_length = 0
        overall_min_nodes = float('inf')
        for i in range(len(nums)):
            max_len_from_node, min_nodes_from_node = dfs(i, -1, set())
            if max_len_from_node > overall_max_length:
                overall_max_length = max_len_from_node
                overall_min_nodes = min_nodes_from_node
            elif max_len_from_node == overall_max_length:
                overall_min_nodes = min(overall_min_nodes, min_nodes_from_node)
        
        return [overall_max_length, overall_min_nodes]
# @lc code=end