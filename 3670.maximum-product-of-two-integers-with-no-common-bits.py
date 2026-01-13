#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
from typing import List
from array import array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = max(nums)
        B = mx.bit_length()
        size = 1 << B
        full = size - 1

        # f[mask] = maximum value in nums with exact bitmask == mask
        f = array('I', [0]) * size
        for v in nums:
            if v > f[v]:
                f[v] = v

        # g[mask] = max f[sub] for all sub ⊆ mask (SOS DP for max)
        g = array('I', f)
        for bit in range(B):
            step = 1 << bit
            block = step << 1
            for start in range(0, size, block):
                # masks in [start+step, start+2*step) have the bit set
                end = start + block
                if end > size:
                    end = size
                base = start + step
                for mask in range(base, end):
                    cand = g[mask - step]
                    if cand > g[mask]:
                        g[mask] = cand

        ans = 0
        for mask, val in enumerate(f):
            if val:
                partner = g[full ^ mask]
                prod = mask * partner
                if prod > ans:
                    ans = prod
        return ans
# @lc code=end
