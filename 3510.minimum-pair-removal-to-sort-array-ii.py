#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        while True:
            n = len(nums)
            min_sum = float('inf')
            min_idx = -1
            # Find adjacent pair with minimum sum
            for i in range(n - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
            # Replace it with their sum if found
            if min_idx != -1:
                nums[min_idx] = min_sum
                del nums[min_idx + 1]
                operations += 1
            # Check if array is non-decreasing after replacement
            sorted_flag = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    sorted_flag = False
                    break
            if sorted_flag:
                break;
        return operations # Return number of operations needed
# @lc code=end