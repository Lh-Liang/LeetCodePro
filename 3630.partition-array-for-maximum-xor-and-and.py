#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
from typing import List

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        full = (1 << n) - 1
        MOD_MASK = (1 << 32) - 1
        INF_AND = MOD_MASK
        xor_all = [0] * (1 << n)
        and_all = [0] * (1 << n)
        and_all[0] = INF_AND
        for mask in range(1, 1 << n):
            i = 0
            tmp = mask
            while (tmp & 1) == 0:
                i += 1
                tmp >>= 1
            sub = mask ^ (1 << i)
            xor_all[mask] = xor_all[sub] ^ nums[i]
            and_all[mask] = and_all[sub] & nums[i]
        total_xor = xor_all[full]
        ans = 0
        for mb in range(1 << n):
            andb = 0 if mb == 0 else and_all[mb]
            xs = total_xor ^ xor_all[mb]
            smask = full ^ mb
            basis = [0] * 32
            for i in range(n):
                if (smask & (1 << i)) == 0:
                    continue
                val = nums[i]
                for j in range(31, -1, -1):
                    if (val & (1 << j)) == 0:
                        continue
                    if basis[j]:
                        val ^= basis[j]
                    else:
                        basis[j] = val
                        break
            M = (~xs) & MOD_MASK
            x = 0
            for k in range(31, -1, -1):
                if (M & (1 << k)) and basis[k] and (x & (1 << k)) == 0:
                    x ^= basis[k]
            extra = x & M
            curr = xs + 2 * extra + andb
            if curr > ans:
                ans = curr
        return ans

# @lc code=end