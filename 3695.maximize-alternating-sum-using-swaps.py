#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        # Step 1: Build DSU to group swappable indices
        n = len(nums)
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        for a, b in swaps:
            union(a, b)
        # Step 2: Group indices by component
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        # Step 3: For each group, assign highest numbers to even-indexed positions
        res = [0]*n
        for indices in groups.values():
            vals = [nums[i] for i in indices]
            indices.sort()
            vals.sort(reverse=True)
            for idx, i in enumerate(indices):
                res[i] = vals[idx]
        # Step 4: Calculate alternating sum
        ans = 0
        for i, v in enumerate(res):
            if i%2==0:
                ans += v
            else:
                ans -= v
        return ans
# @lc code=end