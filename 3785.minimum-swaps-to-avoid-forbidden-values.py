#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        # Track positions of conflicts and potential candidates for swapping
        conflicts = []
        available = []
        # Record indices where nums and forbidden are equal (conflicts)
        for i in range(n):
            if nums[i] == forbidden[i]:
                conflicts.append(i)
            else:
                available.append(i)
        if not conflicts:  # No conflicts initially
            return 0
        # Attempt to resolve all conflicts by swapping with available elements
        swaps = 0
        for i in conflicts:
            found_swap = False
            for j in available:
                if nums[j] != forbidden[i]:  # Valid swap candidate found
                    # Perform swap ensuring it doesn't create new conflict at j's position
                    nums[i], nums[j] = nums[j], nums[i]
                    if nums[j] != forbidden[j]:  # Ensure new position j is not a conflict now
                        available.remove(j)  # Update available list after swap
                        swaps += 1  # Increment swap count
                        found_swap = True
                        break  # Break loop after successful swap
                    else:  # If it results in a conflict revert the change and try next candidate
                        nums[i], nums[j] = nums[j], nums[i]
            if not found_swap:  # If no valid swap was possible for a conflict index
                return -1  # Return -1 as it is not solvable
        return swaps  # Return total number of swaps required to resolve all conflicts.
# @lc code=end