#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

from typing import List
import sys

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        sys.setrecursionlimit(200000)
        n = len(nums)

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        max_val = max(nums) if nums else 0
        last = [-1] * (max_val + 1)

        pathDist = [0] * n  # pathDist[depth] = distance(root -> node at that depth)
        bestLen = 0
        bestNodes = 1

        def dfs(u: int, parent: int, depth: int, dist: int, start: int) -> None:
            nonlocal bestLen, bestNodes
            pathDist[depth] = dist

            x = nums[u]
            prevLast = last[x]
            newStart = start
            if prevLast != -1:
                newStart = max(newStart, prevLast + 1)

            # Evaluate best special path ending at u
            curLen = dist - pathDist[newStart]
            curNodes = depth - newStart + 1
            if curLen > bestLen:
                bestLen = curLen
                bestNodes = curNodes
            elif curLen == bestLen and curNodes < bestNodes:
                bestNodes = curNodes

            # Mark this value occurrence
            last[x] = depth

            for v, w in adj[u]:
                if v == parent:
                    continue
                dfs(v, u, depth + 1, dist + w, newStart)

            # Backtrack
            last[x] = prevLast

        dfs(0, -1, 0, 0, 0)
        return [bestLen, bestNodes]
# @lc code=end
