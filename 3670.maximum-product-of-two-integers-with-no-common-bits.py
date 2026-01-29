#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Determine the number of bits needed based on the maximum value
        max_num = max(nums)
        if max_num == 0: # Constraints say nums[i] >= 1, but safe to check
            return 0
            
        bits = max_num.bit_length()
        limit = 1 << bits
        
        # max_val[mask] stores the maximum value for a specific bitmask
        # Using a list for speed in Python
        max_val = [0] * limit
        unique_nums = []
        for x in nums:
            if max_val[x] == 0:
                unique_nums.append(x)
            if x > max_val[x]:
                max_val[x] = x
        
        # f[mask] will store the maximum value among all numbers whose bitmask is a subset of mask
        f = list(max_val)
        
        # SOS DP (Sum Over Subsets) to compute f[mask] in O(B * 2^B)
        for i in range(bits):
            bit = 1 << i
            for mask in range(limit):
                if mask & bit:
                    # If the subset mask (mask without bit i) has a larger value, update
                    if f[mask ^ bit] > f[mask]:
                        f[mask] = f[mask ^ bit]
        
        ans = 0
        full_mask = limit - 1
        for x in unique_nums:
            # complement contains all bits within our range NOT set in x
            complement = full_mask ^ x
            # f[complement] is the max value whose bits are a subset of complement
            # This means f[complement] & x == 0
            best_partner = f[complement]
            if best_partner > 0:
                product = x * best_partner
                if product > ans:
                    ans = product
        
        return ans
# @lc code=end