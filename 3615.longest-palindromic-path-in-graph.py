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
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        max_len = 1
        def dfs(node, visited, path):
            nonlocal max_len
            if is_palindrome(path):
                max_len = max(max_len, len(path))
            for nei in graph[node]:
                if not (visited & (1 << nei)):
                    dfs(nei, visited | (1 << nei), path + label[nei])
        for start in range(n):
            dfs(start, 1 << start, label[start])
        return max_len
# @lc code=end