#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Store indices for each value (1-50) to process them efficiently
        indices = [[] for _ in range(51)]
        for i, x in enumerate(nums):
            indices[x].append(i)
        
        base_k_count = len(indices[k])
        k_indices = indices[k]
        num_k = len(k_indices)
        max_gain = 0
        
        # Iterate through each possible value v that we want to transform into k
        for v in range(1, 51):
            if v == k or not indices[v]:
                continue
            
            v_indices = indices[v]
            num_v = len(v_indices)
            
            current_running_gain = 0
            best_gain_for_v = 0
            
            ptr_v = 0
            ptr_k = 0
            
            # Apply Kadane's algorithm by merging sorted indices of v (+1) and k (-1)
            while ptr_v < num_v:
                # If there is a 'k' occurring before the current 'v', it acts as a -1
                if ptr_k < num_k and k_indices[ptr_k] < v_indices[ptr_v]:
                    current_running_gain -= 1
                    # Kadane's reset: if gain drops below 0, start a new subarray
                    if current_running_gain < 0:
                        current_running_gain = 0
                    ptr_k += 1
                else:
                    # Current 'v' acts as a +1 gain
                    current_running_gain += 1
                    if current_running_gain > best_gain_for_v:
                        best_gain_for_v = current_running_gain
                    ptr_v += 1
            
            # Note: We don't need to process remaining 'k' indices because 
            # they can only decrease the gain.
            max_gain = max(max_gain, best_gain_for_v)
            
        return base_k_count + max_gain
# @lc code=end