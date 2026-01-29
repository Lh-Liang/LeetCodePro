#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Precompute XOR of all elements to easily find XOR of S_AC
        total_xor = 0
        for x in nums:
            total_xor ^= x
            
        # Iterate through all possible subsets for B
        # mask represents the indices of elements chosen for subsequence B
        for mask in range(1 << n):
            and_b = -1
            xor_ac = total_xor
            s_ac = []
            
            for i in range(n):
                if (mask >> i) & 1:
                    if and_b == -1:
                        and_b = nums[i]
                    else:
                        and_b &= nums[i]
                else:
                    xor_ac ^= 0 # nums[i] is already in total_xor
            
            # If B is empty, AND(B) = 0
            val_b = and_b if and_b != -1 else 0
            
            # xor_ac is the XOR of elements not in B
            # We need to calculate XOR of elements in S_AC
            # which is actually total_xor ^ (XOR of elements in B)
            curr_xor_b = 0
            for i in range(n):
                if (mask >> i) & 1:
                    curr_xor_b ^= nums[i]
            
            target_t = total_xor ^ curr_xor_b
            not_t = ~target_t
            
            # Maximize X & not_t where X is XOR of some subset of S_AC
            basis = []
            for i in range(n):
                if not ((mask >> i) & 1):
                    val = nums[i] & not_t
                    for b in basis:
                        val = min(val, val ^ b)
                    if val > 0:
                        basis.append(val)
                        basis.sort(reverse=True)
            
            max_x_masked = 0
            for b in basis:
                if (max_x_masked ^ b) > max_x_masked:
                    max_x_masked ^= b
            
            current_total = val_b + target_t + 2 * max_x_masked
            if current_total > ans:
                ans = current_total
                
        return ans
# @lc code=end