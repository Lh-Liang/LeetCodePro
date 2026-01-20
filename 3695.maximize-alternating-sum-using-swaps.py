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
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        for p, q in swaps:
            union(p, q)

        val_groups = defaultdict(list)
        even_counts = defaultdict(int)

        for i in range(n):
            root = find(i)
            val_groups[root].append(nums[i])
            if i % 2 == 0:
                even_counts[root] += 1

        total = 0
        for root in val_groups:
            vals = val_groups[root]
            vals.sort(reverse=True)
            e = even_counts[root]
            sum_e = sum(vals[:e])
            total_sum = sum(vals)
            contrib = sum_e - (total_sum - sum_e)
            total += contrib
        return total

# @lc code=end
