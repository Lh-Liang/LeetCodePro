#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
from typing import List
from math import gcd

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 1) Total number of good subarrays by position (not distinct)
        cnt = {0: 1}
        pref = 0
        total_good_pos = 0
        for x in nums:
            pref = (pref + x) % k
            total_good_pos += cnt.get(pref, 0)
            cnt[pref] = cnt.get(pref, 0) + 1

        # 2) Compute positional-good and distinct-good subarrays fully inside each equal-value block
        within_good_pos = 0
        within_good_distinct = 0

        i = 0
        while i < n:
            j = i
            v = nums[i]
            while j < n and nums[j] == v:
                j += 1
            c = j - i

            g = gcd(v, k)
            t = k // g  # L must be multiple of t
            q = c // t

            within_good_distinct += q
            # sum_{p=1..q} (c - p*t + 1)
            within_good_pos += q * (c + 1) - t * (q * (q + 1) // 2)

            i = j

        # 3) Replace within-block positional counts by distinct counts
        return total_good_pos - within_good_pos + within_good_distinct
# @lc code=end
