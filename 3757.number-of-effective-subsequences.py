#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
from typing import List

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Total OR
        T = 0
        for x in nums:
            T |= x

        # Collect bit positions used in T (k <= 20)
        bit_positions = []
        for b in range(20):
            if (T >> b) & 1:
                bit_positions.append(b)
        k = len(bit_positions)
        allMask = (1 << k) - 1

        # Map actual bit value -> compressed index
        bit_to_idx = {}
        for i, b in enumerate(bit_positions):
            bit_to_idx[1 << b] = i

        # freq over compressed masks
        size = 1 << k
        freq = [0] * size
        for x in nums:
            y = x & T
            m = 0
            while y:
                lsb = y & -y
                m |= 1 << bit_to_idx[lsb]
                y -= lsb
            freq[m] += 1

        # SOS DP: g[mask] = sum_{p subset of mask} freq[p]
        g = freq[:]  # counts, not modulo
        for i in range(k):
            step = 1 << i
            for mask in range(size):
                if mask & step:
                    g[mask] += g[mask ^ step]

        # Precompute powers of 2 mod MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] << 1) % MOD

        # Inclusion-exclusion over non-empty bit-subsets
        ans = 0
        for m in range(1, size):
            count0 = g[allMask ^ m]          # elements whose compressed mask has no bit in m
            c = n - count0                    # elements with (p & m) != 0
            term = pow2[n - c]                # 2^(n - c)
            if m.bit_count() & 1:
                ans += term
            else:
                ans -= term

        return ans % MOD

# @lc code=end
