#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        
        for u, v in swaps:
            union(u, v)
        
        # Group indices by connected component
        comps = {}
        for i in range(n):
            root = find(i)
            comps.setdefault(root, []).append(i)
        
        ans = 0
        for indices in comps.values():
            # Count even-indexed positions
            p = sum(1 for i in indices if i % 2 == 0)
            # Values in this component
            vals = [nums[i] for i in indices]
            vals.sort(reverse=True)
            top_sum = sum(vals[:p])          # Sum of largest p values
            total_sum = sum(vals)
            # Contribution = top_sum - (total_sum - top_sum)
            ans += 2 * top_sum - total_sum
        
        return ans
# @lc code=end