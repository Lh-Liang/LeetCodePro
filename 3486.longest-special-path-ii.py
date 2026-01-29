#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#
from typing import List, Tuple, Dict
from collections import defaultdict

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[Tuple[int, int, int]], nums: List[int]) -> List[int]:
        # Build adjacency list for the tree representation
        tree = defaultdict(list)
        for u, v, length in edges:
            tree[u].append((v, length))
            tree[v].append((u, length))
        
        def dfs(node: int, parent: int, visited: Dict[int, int], allow_repeat: bool) -> Tuple[int, int]:
            max_length = 0
            min_nodes = float('inf')
            current_value = nums[node]
            visited[current_value] += 1
            
            for neighbor, edge_length in tree[node]:
                if neighbor == parent:
                    continue
                if visited[nums[neighbor]] == 0 or (allow_repeat and visited[nums[neighbor]] == 1):
                    next_allow_repeat = allow_repeat and (visited[nums[neighbor]] == 0)
                    path_length, path_nodes = dfs(neighbor, node, visited.copy(), next_allow_repeat)
                    total_length = edge_length + path_length
                    total_nodes = path_nodes + 1
                    if total_length > max_length or (total_length == max_length and total_nodes < min_nodes):
                        max_length = total_length
                        min_nodes = total_nodes
            
            visited[current_value] -= 1
            return max_length, min_nodes if min_nodes != float('inf') else len(tree)
        
        # Start DFS from root node 0 with allowance for one repeat value on path
        max_path_len, min_num_nodes = dfs(0, -1, defaultdict(int), True)
        return [max_path_len, min_num_nodes]
# @lc code=end