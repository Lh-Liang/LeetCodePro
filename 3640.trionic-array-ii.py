#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        
        # Arrays to store max increasing/decreasing sums up to or from each index
        increasing_left = [0] * n
        decreasing = [0] * n
        increasing_right = [0] * n
        
        # Calculate increasing sums from left to right
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing_left[i] = increasing_left[i - 1] + nums[i]
            else:
                increasing_left[i] = nums[i]
            
        # Calculate decreasing sums from right to left and prepare right-increasing sums
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                decreasing[i] = decreasing[i + 1] + nums[i]
            else:
                decreasing[i] = nums[i]
            
            if nums[i] < nums[i + 1]:
                increasing_right[i] = increasing_right[i + 1] + nums[i]
            else:
                increasing_right[i] = nums[i]
        
        max_sum = float('-inf')
        # Find max trionic subarray sum by combining results from above arrays
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                if nums[q] > nums[q - 1]: # Ensure q starts an increase again after decrease
                    l_sum = increasing_left[p]
                    d_sum = decreasing[q]
                    r_sum = increasing_right[q + 1]
                    max_sum = max(max_sum, l_sum + d_sum + r_sum)
                    
        return max_sum
# @lc code=end