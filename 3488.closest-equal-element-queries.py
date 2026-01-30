#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        import bisect
        n = len(nums)
        val_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            val_to_indices[val].append(idx)
        res = []
        for q in queries:
            v = nums[q]
            indices = val_to_indices[v]
            if len(indices) == 1:
                res.append(-1)
                continue
            i = bisect.bisect_left(indices, q)
            min_dist = n
            for ni in [indices[i % len(indices)], indices[(i-1) % len(indices)]]:
                if ni == q: continue  # Ensure not comparing the index to itself
                dist = min((q - ni) % n, (ni - q) % n)
                if dist > 0: min_dist = min(min_dist, dist)
            if min_dist == n:
                res.append(-1)
            else:
                res.append(min_dist)
        return res
# @lc code=end