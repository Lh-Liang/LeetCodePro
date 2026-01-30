#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        res = []
        for li, ri in queries:
            sub = nums[li:ri+1]
            mods = [x % k for x in sub]
            if not all(m == mods[0] for m in mods):
                res.append(-1)
                continue
            arr = sorted([x // k for x in sub])
            m = len(arr)
            median = arr[m//2]
            ops = sum(abs(x - median) for x in arr)
            res.append(ops)
        return res
# @lc code=end