#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        pos_dict = defaultdict(list)
        for i in range(n):
            pos_dict[nums[i]].append(i)
        ans = [-1] * n
        for pos in pos_dict.values():
            k = len(pos)
            if k < 2:
                continue
            for i in range(k):
                curr = pos[i]
                prev_i = (i - 1) % k
                next_i = (i + 1) % k
                prev_p = pos[prev_i]
                next_p = pos[next_i]
                d1 = min(abs(curr - prev_p), n - abs(curr - prev_p))
                d2 = min(abs(curr - next_p), n - abs(curr - next_p))
                ans[curr] = min(d1, d2)
        return [ans[q] for q in queries]
# @lc code=end