#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        n = len(nums)
        full_or = 0
        for num in nums:
            full_or |= num
        bit_list = [b for b in range(32) if full_or & (1 << b)]
        k = len(bit_list)
        if k == 0:
            return 0
        MOD = 10**9 + 7
        freq = [0] * (1 << k)
        for num in nums:
            proj = 0
            for j in range(k):
                if num & (1 << bit_list[j]):
                    proj |= (1 << j)
            freq[proj] += 1
        prefix = freq[:]
        for i in range(k):
            for s in range(1 << k):
                if s & (1 << i):
                    prefix[s] += prefix[s ^ (1 << i)]
        popc = [0] * (1 << k)
        for s in range(1 << k):
            popc[s] = popc[s >> 1] + (s & 1)
        ans = 0
        ALL = (1 << k) - 1
        for state in range(1, 1 << k):
            comp = ALL ^ state
            num_zero = prefix[comp]
            cnt = n - num_zero
            pop = popc[state]
            sign = 1 if pop % 2 == 1 else -1
            poww = pow(2, n - cnt, MOD)
            contrib = (sign * poww) % MOD
            ans = (ans + contrib) % MOD
        return ans
# @lc code=end