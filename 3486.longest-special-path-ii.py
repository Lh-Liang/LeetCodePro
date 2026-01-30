#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict, Counter
        
        # Step 1: Build graph from edges
        graph = defaultdict(list)
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))  # It's undirected
        
        # Step 2 & 3: DFS to find longest special path
        def dfs(node, parent):
            max_len = [0]
            min_nodes = [float('inf')]
            visited_values = Counter()
            
            def dfs_visit(node, current_length):
                visited_values[nums[node]] += 1
                # Check if more than one value is repeated more than once or a single value more than twice.
                if len([v for v in visited_values.values() if v > 1]) > 1:
                    visited_values[nums[node]] -= 1
                    return
                
                local_max_len = current_length
                local_min_nodes = sum(visited_values.values())
                if local_max_len > max_len[0]:
                    max_len[0] = local_max_len
                    min_nodes[0] = local_min_nodes
                elif local_max_len == max_len[0]:
                    min_nodes[0] = min(min_nodes[0], local_min_nodes)
                
                for neighbor, edge_length in graph[node]:
                    if neighbor != parent:
                        dfs_visit(neighbor, current_length + edge_length)
                visited_values[nums[node]] -= 1
            
            dfs_visit(node, 0)
            return max_len[0], min_nodes[0]
        
        result_length, result_min_nodes = dfs(0, -1)  # Start DFS from root node '0' with no parent (-1)
        return [result_length, result_min_nodes] if result_min_nodes != float('inf') else [0, 1]
# @lc code=end