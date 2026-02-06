#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
from typing import List
import collections

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        def min_operations_in_subarray(subarray):
            # Sort the subarray to find a potential target value easier.
            subarray.sort()
            n = len(subarray)
            
            # Calculate prefix sums for efficient calculation of operations needed.
            prefix_sum = [0] * (n + 1)
            for i in range(n):
                prefix_sum[i + 1] = prefix_sum[i] + subarray[i]
            
            # Try making all elements equal to each element in the sorted array and calculate cost.
            min_operations = float('inf')
            for i in range(n):
                # Target value is subarray[i], calculate cost to make all elements equal to this.
                left_operations = i * subarray[i] - prefix_sum[i]
                right_operations = (prefix_sum[n] - prefix_sum[i + 1]) - (n - i - 1) * subarray[i]
                total_operations = left_operations + right_operations
                min_operations = min(min_operations, total_operations)
            
            return min_operations // k if min_operations % k == 0 else -1
        
        results = []
        for li, ri in queries:
            subarray = nums[li:ri+1]
            if len(set((x % k) for x in subarray)) > 1:
                results.append(-1)  # Not possible if remainders modulo k are not all same.
            else:
                results.append(min_operations_in_subarray(subarray))
        return results
# @lc code=end