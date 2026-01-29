#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Initial frequency of k
        total_k = nums.count(k)
        
        # We want to maximize: total_k + (count of v in subarray - count of k in subarray)
        # This is equivalent to Kadane's where v is +1 and k is -1.
        # Since values are small (1-50), we can track the max gain for each value v.
        
        # max_gain[v] stores the maximum gain found so far using value v
        # current_gain[v] stores the running Kadane sum for value v
        max_gain = [0] * 51
        current_gain = [0] * 51
        
        for x in nums:
            if x == k:
                # If we encounter k, it's a -1 for all potential values v
                for v in range(1, 51):
                    if v == k: continue
                    current_gain[v] -= 1
                    # If current_gain drops below 0, reset (standard Kadane's)
                    if current_gain[v] < 0:
                        current_gain[v] = 0
            else:
                # If we encounter x (where x != k), it's a +1 for value x
                current_gain[x] += 1
                if current_gain[x] > max_gain[x]:
                    max_gain[x] = current_gain[x]
        
        return total_k + max(max_gain)
# @lc code=end