# @lc app=leetcode id=3615 lang=python3
# [3615] Longest Palindromic Path in Graph

# @lc code=start
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        from collections import defaultdict
        
        # Build adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def is_palindrome(s):
            return s == s[::-1]

        def dfs(node, visited, path):
            nonlocal max_len
            # Mark this node as visited
            visited[node] = True
            # Add current node's label to the path
            new_path = path + label[node]
            # Check if current path is palindrome and update max length
            if is_palindrome(new_path):
                max_len = max(max_len, len(new_path))
            # Explore adjacent nodes
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, new_path)
            # Backtrack to explore other paths (unvisit this node)
            visited[node] = False
        
        max_len = 0
        for start_node in range(n):
            # Start DFS from each node with no nodes visited initially and empty path string
            dfs(start_node, [False] * n, '')
        return max_len
# @lc code=end