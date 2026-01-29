#
# @lc app=leetcode id=3757 lang=python3
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        total_or = 0
        for x in nums:
            total_or |= x
        
        if total_or == 0:
            return 0
            
        # Identify relevant bits (those present in total_or)
        bits = []
        for i in range(21):
            if (total_or >> i) & 1:
                bits.append(i)
        
        m = len(bits)
        # count[mask] will store how many nums[i] have their relevant bits as a submask of mask
        # We map the bits of total_or to 0...m-1
        count = [0] * (1 << m)
        for x in nums:
            mask = 0
            for i in range(m):
                if (x >> bits[i]) & 1:
                    mask |= (1 << i)
            count[mask] += 1
            
        # SOS DP (Sum Over Subsets) to find f(mask): number of elements that are submasks of mask
        for i in range(m):
            for mask in range(1 << m):
                if (mask >> i) & 1:
                    count[mask] += count[mask ^ (1 << i)]
        
        # Power of 2 precomputation
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        # Inclusion-Exclusion to find number of subsets whose OR is exactly total_or (mask (1<<m)-1)
        ineffective_subsets_count = 0
        full_mask = (1 << m) - 1
        for mask in range(1 << m):
            # Parity of bits missing from full_mask
            bits_diff = bin(full_mask ^ mask).count('1')
            term = pow2[count[mask]]
            if bits_diff % 2 == 1:
                ineffective_subsets_count = (ineffective_subsets_count - term) % MOD
            else:
                ineffective_subsets_count = (ineffective_subsets_count + term) % MOD
        
        # Total subsequences = 2^n
        # Effective = Total - Ineffective
        total_subsequences = pow2[n]
        ans = (total_subsequences - ineffective_subsets_count) % MOD
        return ans
# @lc code=end