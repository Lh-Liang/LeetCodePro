#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        maxlen = 1
        visited_global = set()

        def dfs(node, visited_mask, path):
            nonlocal maxlen
            key = (node, visited_mask)
            if key in visited_global:
                return
            visited_global.add(key)
            # Prune: if the current path + all remaining nodes can't beat maxlen, stop
            remaining = n - bin(visited_mask).count('1')
            if len(path) + remaining <= maxlen:
                return
            if is_palindrome(path):
                maxlen = max(maxlen, len(path))
            for nei in graph[node]:
                if not (visited_mask & (1 << nei)):
                    dfs(nei, visited_mask | (1 << nei), path + label[nei])

        # To avoid mirrored duplicate paths, always start from each node but only proceed in a fixed order
        for start in range(n):
            dfs(start, 1 << start, label[start])

        # Final verification (implicit in the unique (node, mask) states and full path exploration)
        return maxlen
# @lc code=end