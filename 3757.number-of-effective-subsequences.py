#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        from collections import defaultdict
        MOD = 10 ** 9 + 7
        n = len(nums)
        total_or = 0
        for x in nums:
            total_or |= x
        # Find all bits set in total_or
        bits = []
        for i in range(21):
            if (total_or >> i) & 1:
                bits.append(i)
        m = len(bits)
        # For each bit, record which indices have it set
        bit_indices = [set() for _ in range(m)]
        for idx, x in enumerate(nums):
            for j, b in enumerate(bits):
                if (x >> b) & 1:
                    bit_indices[j].add(idx)
        ans = 0
        # Inclusion-Exclusion over all non-empty subsets of bits
        for mask in range(1, 1 << m):
            cover = set()
            cnt_bits = 0
            for j in range(m):
                if (mask >> j) & 1:
                    cover |= bit_indices[j]
                    cnt_bits += 1
            cnt = len(cover)
            add = pow(2, cnt, MOD) - 1
            if cnt_bits % 2 == 1:
                ans = (ans + add) % MOD
            else:
                ans = (ans - add) % MOD
        return ans
# @lc code=end