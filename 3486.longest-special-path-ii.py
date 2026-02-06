#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict, deque
        n = len(nums)
        graph = defaultdict(list)
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        def dfs(node, parent, seen):
            max_length = 0
            min_nodes = float('inf')
            seen.add(nums[node])
            for neighbor, length in graph[node]:
                if neighbor == parent:
                    continue
                if nums[neighbor] not in seen or (nums.count(nums[neighbor]) == 1): # Allow one duplicate value on path. 
                    new_length, new_min_nodes = dfs(neighbor, node, seen.copy()) # Copy seen to handle backtracking correctly. 
                    new_length += length # Add edge length to current path. 
                    if new_length > max_length:
                        max_length = new_length # Update max path length found so far. 
                        min_nodes = new_min_nodes + 1 # Update min nodes on this max path. 
                    elif new_length == max_length:
                        min_nodes = min(min_nodes, new_min_nodes + 1) # Choose smallest nodes count for equal lengths paths. 
            return max_length, min_nodes if min_nodes != float('inf') else 1 # Return results ensuring minimum nodes is valid. 
dfs(0, -1, set())