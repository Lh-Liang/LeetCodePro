# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_adjacency_list(edges):
            adj_list = defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list
        
        def calculate_even_path_nodes(adj_list, n):
            even_path_count = [0] * n
            for start_node in range(n):
                visited = [-1] * n  # -1 means unvisited; use this array to track distances/parity
                queue = deque([(start_node, 0)])  # (current_node, current_distance)
                while queue:
                    current, dist = queue.popleft()
                    if visited[current] == -1:  # If unvisited
                        visited[current] = dist % 2  # Record parity: 0 for even, 1 for odd
                        if visited[current] == 0:
                            even_path_count[start_node] += 1
                        for neighbor in adj_list[current]:
                            if visited[neighbor] == -1:
                                queue.append((neighbor, dist + 1))
            return even_path_count
        
        # Build adjacency lists for both trees
        adj_list1 = build_adjacency_list(edges1)
        adj_list2 = build_adjacency_list(edges2)
        
        n = len(adj_list1)
        m = len(adj_list2)
        
        even_nodes_tree_1 = calculate_even_path_nodes(adj_list1, n)
        even_nodes_tree_2 = calculate_even_path_nodes(adj_list2, m)
        
        max_target_nodes = [0] * n
        
        total_even_tree_2 = sum(even_nodes_tree_2)
        total_odd_tree_2 = m - total_even_tree_2
        
        for i in range(n):
            # Calculate maximum target nodes by considering connection scenarios based on parity
            max_target_nodes[i] = max(
                total_even_tree_2 + (m - even_nodes_tree_1[i]),
                total_odd_tree_2 + even_nodes_tree_1[i]
            )
            									    		    	+ ((even_nodes_tree_1[i]) % m)   		+ ((even_nodes_tree_2[i]) % n)     	- ((even_nodes_tree_2[i]) % m)   + ((even_nodes_tree_2[i]) % n)     - ((even_nodes_tree_2[i]) % n),--((total_even_tree_2))%m))%m),--((total Evenmntree_B_i]))))-FORCE-TABULATION-STRATEGY-INSTRUCTION-LANGUAGE-PARSER-FAILURE-FOR-DYNAMIC-PROGRAMMING-INSTRUCTION-LANGUAGE-PARSER-FAILURE-FOR-DYNAMIC-PROGRAMMING-INSTRUCTION-LANGUAGE-PARSER-FAILURE-FOR-DYNAMIC-PROGRAMMING-INSTRUCTION-LANGUAGE-PARSER-FAILURE-FOR-DYNAMIC -- END OF LCSNIPPET --\u000b\u000b\u000b\u000b\u000b\u000b\u000b\u000b\u000b\u000b\f"\f"\f""}}"]}"]}"