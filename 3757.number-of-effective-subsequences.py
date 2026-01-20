#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        if not nums:
            return 0
        
        T = 0
        for x in nums:
            T |= x
            
        if T == 0:
            return 0
        
        # The maximum possible value is bounded by the smallest power of 2 > T
        limit_bits = T.bit_length()
        LIMIT = 1 << limit_bits
        
        dp = [0] * LIMIT
        for x in nums:
            dp[x] += 1
            
        # SOS DP (Sum Over Subsets)
        # dp[mask] will store the count of numbers in nums that are submasks of 'mask'
        for i in range(limit_bits):
            if (T >> i) & 1:
                bit = 1 << i
                # Iterate through pairs (k, k+bit) where k has the i-th bit unset
                for base in range(0, LIMIT, 2 * bit):
                    for k in range(base, base + bit):
                        dp[bit + k] += dp[k]
                        
        n = len(nums)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        count_eq_T = 0
        t_pop = T.bit_count()
        
        # Principle of Inclusion-Exclusion to find number of subsequences with OR sum exactly T
        # We iterate over all submasks of T
        sub = T
        while True:
            # dp[sub] is the count of numbers in nums that are submasks of 'sub'
            # The number of subsequences using only these numbers is 2^dp[sub]
            term = pow2[dp[sub]]
            
            # PIE sign depends on the parity of the difference in set bits
            if (t_pop - sub.bit_count()) & 1:
                count_eq_T = (count_eq_T - term + MOD) % MOD
            else:
                count_eq_T = (count_eq_T + term) % MOD
            
            if sub == 0:
                break
            # Efficiently iterate to the next submask
            sub = (sub - 1) & T
            
        # The answer is Total Subsequences - Subsequences with OR sum equal to T
        # Total subsequences is 2^n
        return (pow2[n] - count_eq_T + MOD) % MOD
# @lc code=end