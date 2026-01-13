#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
from typing import List

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Build prefix sums of mapped array: +1 if == target else -1
        pref = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            pref[i] = pref[i - 1] + (1 if x == target else -1)

        # Coordinate compression of prefix sums
        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}  # 1-indexed for Fenwick

        bit = Fenwick(len(vals))
        ans = 0

        for s in pref:
            r = rank[s]
            # count of previous prefix sums strictly smaller than s
            ans += bit.sum(r - 1)
            bit.add(r, 1)

        return ans
# @lc code=end
