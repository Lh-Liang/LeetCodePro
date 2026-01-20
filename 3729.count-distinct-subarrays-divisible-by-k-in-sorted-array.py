#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Calculate count of all subarrays with sum divisible by k.
        # We use prefix sums modulo k.
        prefix_mod_count = {0: 1}
        current_sum = 0
        total_divisible = 0
        
        for x in nums:
            current_sum = (current_sum + x) % k
            count = prefix_mod_count.get(current_sum, 0)
            total_divisible += count
            prefix_mod_count[current_sum] = count + 1
            
        # Step 2: Adjust for duplicates.
        # In a sorted array, duplicate subarrays arise only from blocks of identical elements.
        # Specifically, if nums[i] == nums[j], the subarray nums[i...j] consists of identical values.
        # We only want to count such subarrays if they start at the beginning of the block.
        # So we subtract all occurrences within blocks and add back the ones starting at the block head.
        
        adjustment = 0
        import math
        
        i = 0
        while i < n:
            j = i
            # Find the extent of the current block of identical values
            while j < n and nums[j] == nums[i]:
                j += 1
            
            # Block is nums[i...j-1]
            length = j - i
            val = nums[i]
            
            # Calculate gcd to find the period of lengths that result in a sum divisible by k
            # sum(len) = len * val. We need len * val % k == 0.
            # This means len must be a multiple of k / gcd(val, k).
            g = math.gcd(val, k)
            target = k // g
            
            # max_m is the number of valid lengths (multiples of target) that fit in the block
            max_m = length // target
            
            if max_m > 0:
                # Subtract all valid pairs strictly inside this block.
                # For a valid length L = m * target, there are (length - L + 1) such subarrays.
                # We sum this quantity for m = 1 to max_m.
                # Sum = sum(length + 1 - m * target) = (length + 1) * max_m - target * sum(m)
                subtract_count = (length + 1) * max_m - target * (max_m * (max_m + 1) // 2)
                
                # Add back only the unique ones (starting at the beginning of the block).
                # There is exactly one such subarray for each valid length.
                add_count = max_m
                
                adjustment += (add_count - subtract_count)
            
            i = j
            
        return total_divisible + adjustment

# @lc code=end