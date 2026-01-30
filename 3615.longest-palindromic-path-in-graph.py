#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        from collections import defaultdict
        def is_palindrome(s):
            return s == s[::-1]
        
        # Create adjacency list for graph representation
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Depth First Search function to explore paths
        def dfs(node, visited, path):
            nonlocal max_length
            if len(path) > 1 and is_palindrome(path):
                max_length = max(max_length, len(path))  # Update max length if palindrome found
            
            visited.add(node)  # Mark node as visited
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, path + label[neighbor])  # Recursive DFS call with updated path string
            visited.remove(node)  # Backtrack by removing node from visited set after exploring its paths fully
        
nmax_length = 1  # At least one node itself is a palindrome of length 1 initially assumed. 
dfs(0, set(), label[0])  # Start DFS from each node (only needed once due to undirected nature of graph). 
nreturn max_length

# @lc code=end