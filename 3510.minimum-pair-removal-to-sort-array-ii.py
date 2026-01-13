#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        
        if len(nums) == 1 or is_non_decreasing(nums):
            return 0
        
        operations = 0
        arr = nums[:]
        
        while not is_non_decreasing(arr):
            # Find leftmost pair with minimum sum
            min_sum = float('inf')
            min_idx = -1
            
            for i in range(len(arr) - 1):
                pair_sum = arr[i] + arr[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
            
            # Merge the pair at min_idx and min_idx+1
            arr[min_idx] += arr[min_idx + 1]
            del arr[min_idx + 1]
            operations += 1
        
        return operations
# @lc code=end