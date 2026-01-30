#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#
# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        from collections import defaultdict
        n = len(nums)
        or_all = 0
        for x in nums:
            or_all |= x
        # Find bits in or_all
        bits = []
        for k in range(0, 21):
            if (or_all >> k) & 1:
                bits.append(k)
        # For each bit, get indices where nums[i] has that bit
        bit_indices = {}
        for b in bits:
            bit_indices[b] = []
        for i, x in enumerate(nums):
            for b in bits:
                if (x >> b) & 1:
                    bit_indices[b].append(i)
        m = len(bits)
        ans = 0
        # Inclusion-Exclusion over all non-empty subsets of bits
        for mask in range(1, 1 << m):
            involved = set(range(n))
            sign = -1
            for j in range(m):
                if (mask >> j) & 1:
                    involved &= set(bit_indices[bits[j]])
                    sign *= -1
            if not involved:
                continue
            cnt = len(involved)
            # Number of non-empty subsequences of these indices
            ways = pow(2, cnt, MOD) - 1
            ans = (ans + sign * ways) % MOD
        return ans % MOD
# @lc code=end