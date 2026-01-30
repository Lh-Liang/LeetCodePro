#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # Flatten the grid into a list of tuples (value, row_index)
        elements = []
        for i, row in enumerate(grid):
            # Sort each row in descending order to consider largest values first
            sorted_row = sorted(row, reverse=True)[:limits[i]]
            for value in sorted_row:
                elements.append((value, i))
        
        # Sort all collected elements by their value in descending order
        elements.sort(reverse=True, key=lambda x: x[0])
        
        max_sum = 0
        count = 0  # Track number of selected elements
        used_limits = [0] * len(grid)  # Track used limits per row
        
        # Select up to k largest values respecting per-row limits
        for value, idx in elements:
            if count < k and used_limits[idx] < limits[idx]:
                max_sum += value
                used_limits[idx] += 1
                count += 1
            if count == k:
                break
        return max_sum
# @lc code=end