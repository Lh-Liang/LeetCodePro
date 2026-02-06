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
        
        # Initialize adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # DFS function to find all paths
        def dfs(node, path):
            nonlocal max_len
            if is_palindrome(path):
                max_len = max(max_len, len(path))
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, path + label[neighbor])
            visited.remove(node)
        
        max_len = 0
        for start_node in range(n):
            visited = set()
            dfs(start_node, label[start_node])      
        return max_len  
# @lc code=end