#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        offset = n + 1
        tree = [0] * (2 * n + 3)

        def fen_update(val, delta=1):
            idx = val + offset
            while idx < len(tree):
                tree[idx] += delta
                idx += idx & -idx

        def fen_query(val):
            idx = val + offset
            res = 0
            while idx > 0:
                res += tree[idx]
                idx -= idx & -idx
            return res

        ans = 0
        pre = 0
        fen_update(0)
        for num in nums:
            pre += 1 if num == target else -1
            ans += fen_query(pre - 1)
            fen_update(pre)
        return ans

# @lc code=end