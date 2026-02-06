#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        graph = defaultdict(list)
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        def dfs(node, parent, visited_values, can_duplicate):
            visited_values.add(nums[node])
            max_path_length = 0
            min_nodes = float('inf')
            for neighbor, length in graph[node]:
                if neighbor != parent:
                    if nums[neighbor] not in visited_values or can_duplicate:
                        new_duplicate_flag = can_duplicate and nums[neighbor] in visited_values
                        sub_path_length, sub_node_count = dfs(
                            neighbor,
                            node,
                            visited_values.copy(),
                            not new_duplicate_flag  # allow duplication only once
                        )
                        # Check special path conditions here and update max/min if applicable
                        total_length = sub_path_length + length
                        total_nodes = sub_node_count + 1  # include current node in count
                        if total_length > max_path_length:
                            max_path_length = total_length
                            min_nodes = total_nodes
                        elif total_length == max_path_length:
                            min_nodes = min(min_nodes, total_nodes)
            if max_path_length == 0:  # No valid path found; consider single node as a trivial path.
                return (0, len(visited_values)) 
            return (max_path_length, min_nodes)
        
        result = dfs(0, -1, set(), True) # start DFS from root node with allowance for one duplicate 
        return [result[0], result[1]] # finalize result logic based on problem constraints 
# @lc code=end