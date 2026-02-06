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
            min_sum = float('inf')
            min_index = -1
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    pair_sum = nums[i] + nums[i + 1]
                    if pair_sum < min_sum:
                        min_sum = pair_sum
                        min_index = i
            if min_index == -1:
                break
            # Merge pair at min_index with minimum sum
            nums[min_index] = min_sum
            del nums[min_index + 1]
            operations += 1
        return operations
# @lc code=end