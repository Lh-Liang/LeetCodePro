#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # Initialize result list for answers
        ans = []
        
        # Process each query separately
        for li, ri in queries:
            # Extract subarray from nums based on current query indices
            subarray = nums[li:ri+1]
            
            # Determine unique values in the subarray that can be transformed into each other via operations of size k
            unique_values = set(subarray)
            can_be_equalized = len(unique_values) == 1 or all((abs(x - y) % k == 0) for x in unique_values for y in unique_values)
            
            if not can_be_equalized:
                ans.append(-1)  # Not possible to equalize subarray with given k
                continue
                
            # Calculate minimum operations needed to make all elements in subarray equal
            min_operations = float('inf')
            target_value = max(subarray)  # Example choice of target value; could be optimized further
            current_operations = sum(abs(x - target_value) // k for x in subarray if (x - target_value) % k == 0)
            min_operations = min(min_operations, current_operations)
            
            ans.append(min_operations if min_operations != float('inf') else -1)  # Append result for current query
        
        return ans  # Return list of results for each query processed
# @lc code=end