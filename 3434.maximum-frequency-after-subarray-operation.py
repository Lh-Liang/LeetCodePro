#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Count original occurrences of k
        base_k = 0
        for x in nums:
            if x == k:
                base_k += 1
        
        max_gain = 0
        # Constraints say nums[i] is between 1 and 50.
        # We iterate through all possible values that could be changed to k.
        unique_vals = set(nums)
        
        for v in unique_vals:
            if v == k:
                continue
            
            current_gain = 0
            best_v_gain = 0
            
            # Kadane's algorithm to maximize: (count of v) - (count of k)
            for x in nums:
                if x == v:
                    current_gain += 1
                elif x == k:
                    current_gain -= 1
                
                if current_gain < 0:
                    current_gain = 0
                
                if current_gain > best_v_gain:
                    best_v_gain = current_gain
            
            if best_v_gain > max_gain:
                max_gain = best_v_gain
                
        return base_k + max_gain
# @lc code=end