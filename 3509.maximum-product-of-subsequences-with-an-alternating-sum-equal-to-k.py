#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        max_sum = 12 * n
        if k < -max_sum or k > max_sum:
            return -1

        offset = max_sum
        L = 2 * max_sum + 1
        mask = (1 << L) - 1
        target_bit = 1 << (k + offset)

        # dp0[p] -> bitset of sums for non-empty subsequences with product p and length parity 0
        # dp1[p] -> bitset of sums for non-empty subsequences with product p and length parity 1
        dp0 = [0] * (limit + 1)
        dp1 = [0] * (limit + 1)

        for x in nums:
            prev0, prev1 = dp0, dp1
            new0 = prev0[:]  # skipping x
            new1 = prev1[:]

            # Start a new subsequence with just [x]
            if x <= limit:
                # sum = +x, parity becomes 1
                new1[x] |= 1 << (x + offset)

            if x == 0:
                ub = limit
            else:
                ub = limit // x

            # Extend existing subsequences
            for p in range(ub + 1):
                np = p * x

                b0 = prev0[p]
                if b0:
                    # parity 0 -> parity 1, sum + x
                    new1[np] |= (b0 << x) & mask

                b1 = prev1[p]
                if b1:
                    # parity 1 -> parity 0, sum - x
                    new0[np] |= (b1 >> x)

            dp0, dp1 = new0, new1

        for p in range(limit, -1, -1):
            if (dp0[p] & target_bit) or (dp1[p] & target_bit):
                return p
        return -1
# @lc code=end
