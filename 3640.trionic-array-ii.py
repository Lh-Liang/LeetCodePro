#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        
        inc1 = float('-inf')  # max sum of strictly increasing subarray (>= 2 elements)
        dec = float('-inf')   # max sum of inc-dec pattern
        inc2 = float('-inf')  # max sum of trionic pattern (inc-dec-inc)
        
        result = float('-inf')
        
        for i in range(1, n):
            new_inc1 = float('-inf')
            new_dec = float('-inf')
            new_inc2 = float('-inf')
            
            if nums[i] > nums[i-1]:
                # Continuing or starting first increase
                new_inc1 = max(nums[i-1] + nums[i], inc1 + nums[i])
                # Continuing second increase
                new_inc2 = max(dec + nums[i], inc2 + nums[i])
            elif nums[i] < nums[i-1]:
                # Continuing or starting decrease
                new_dec = max(inc1 + nums[i], dec + nums[i])
            
            inc1 = new_inc1
            dec = new_dec
            inc2 = new_inc2
            result = max(result, inc2)
        
        return result
# @lc code=end