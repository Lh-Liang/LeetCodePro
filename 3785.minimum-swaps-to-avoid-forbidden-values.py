#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        swaps = 0
        for i in range(n):
            if nums[i] == forbidden[i]:
                for j in range(i + 1, n):
                    if nums[j] != forbidden[j] and nums[j] != forbidden[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        swaps += 1
                        break
                else:
                    return -1 # No valid swap found for position i
        return swaps # Return total number of swaps made.
# @lc code=end