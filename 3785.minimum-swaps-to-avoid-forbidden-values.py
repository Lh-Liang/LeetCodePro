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
                found = False
                for j in range(i + 1, n):
                    if nums[j] != forbidden[i] and nums[j] != forbidden[j]:
                        # Swap elements at i and j
                        nums[i], nums[j] = nums[j], nums[i]
                        swaps += 1
                        found = True
                        break
                # If no valid swap was found, it's impossible to solve
                if not found:
                    return -1
        # Verify final configuration (though this is implied by construction)
        for k in range(n):
            if nums[k] == forbidden[k]:
                return -1
        return swaps # @lc code=end