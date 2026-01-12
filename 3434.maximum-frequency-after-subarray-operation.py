#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total_k = 0
        # max_gains[v] will store the maximum subarray sum (Count(v) - Count(k)) seen so far for value v
        max_gains = [0] * 51
        # current_gains[v] will store the current running Kadane sum for value v
        current_gains = [0] * 51
        
        # Identify distinct values in nums to potentially skip unnecessary iterations
        distinct_values = set(nums)
        if k in distinct_values:
            distinct_values.remove(k)
            
        for x in nums:
            if x == k:
                total_k += 1
                # For every other potential value v, seeing a 'k' decreases the potential gain
                for v in distinct_values:
                    if current_gains[v] > 0:
                        current_gains[v] -= 1
            else:
                # Seeing the value x increases the potential gain for that specific value
                current_gains[x] += 1
                if current_gains[x] > max_gains[x]:
                    max_gains[x] = current_gains[x]
        
        # The result is the original count of k plus the maximum gain we found
        return total_k + max(max_gains)
# @lc code=end