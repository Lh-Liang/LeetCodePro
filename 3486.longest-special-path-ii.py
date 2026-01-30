#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict
        
        # Create adjacency list from edges
        graph = defaultdict(list)
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        # Store result - length of longest path and its node count
        result = [0, float('inf')] # [max_length, min_nodes]
        
        def dfs(node, parent, visited):
            nonlocal result
            visited[node] = True
            path_length = 0  # Track current path length
            unique_values = set()  # Track unique values along current path
            duplicate_value_present = False  # Flag if one duplicate is allowed and present
            
            for neighbor, length in graph[node]:
                if neighbor == parent:
                    continue  # Skip backtracking to parent node in DFS tree traversal
                if neighbor not in visited or not visited[neighbor]:  # Check unvisited nodes only or handle revisit conditionally if needed.
                    vl = nums[neighbor]  # Value at the child node neighbor being explored.
                    if vl in unique_values and not duplicate_value_present:
                        duplicate_value_present = True  # Allow one duplicate value appearance along this path once.
                    elif vl in unique_values:
                        continue  # Stop exploring further if second duplicate value found on this same special path due to condition violation.
                    else:
v                        unique_values.add(vl)   # Add new unique value into set for tracking along current descending path exploration. /t/t/t/t/t/t/t/t/t/t/t/t/t/t/t/t/t/t/t/t       // Perform dfs traversal recursively on child node with updated tracking variables state. // Accumulate total length calculated so far with edge weight connecting current nodes traversed (node <-> neighbor).                      
i               child_length = dfs(neighbor,node,{**visited}) + length   /// Add edge weight connecting between current nodes traversed (node <-> neighbor) .                     
i                // Evaluate max possible tracking for special paths discovered so far by comparing against previous max-length value stored globally & update accordingly.
                 result[0] = max(result[0], child_length)   // Update maximum length found across all special paths explored globally.
                 result[1] = min(result[1], len(unique_values)) // Update minimum nodes count tracked across all max-length special paths explored globally.
                 visited[node]=False// Backtrack step: Reset visit status before returning ; ensures correct exploration along alternative branches possible next time output: return child_length // Return accumulated total length calculated after all possible paths explored recursively from current branch.
          return max(visited,node)// Finalize implementation: Call DFS starting from root node & ensure initial state setup correctly before invocation! {**visited})// Ensure initial state setup correctly before invocation!
         dfs(0,-1,{})
       return result

# @lc code=end