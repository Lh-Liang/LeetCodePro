#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        def find(p: list[int], i: int) -> int:
            if p[i] != i:
                p[i] = find(p, p[i])
            return p[i]
        
        def union(p: list[int], rank: list[int], a: int, b: int):
            pa = find(p, a)
            pb = find(p, b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                p[pa] = pb
            elif rank[pa] > rank[pb]:
                p[pb] = pa
            else:
                p[pb] = pa
                rank[pa] += 1
        
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n
        for a, b in swaps:
            union(parent, rank, a, b)
        
        groups = defaultdict(list)
        for i in range(n):
            groups[find(parent, i)].append(i)
        
        ans = 0
        for idxs in groups.values():
            vals = sorted(nums[i] for i in idxs, reverse=True)
            ne = sum(1 for i in idxs if i % 2 == 0)
            ans += sum(vals[:ne]) - sum(vals[ne:])
        return ans

# @lc code=end