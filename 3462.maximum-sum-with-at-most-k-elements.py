#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # Step 1: For each row, sort in descending order and select up to limits[i] largest elements
        potential_elements = []
        for i in range(len(grid)):
            sorted_row = sorted(grid[i], reverse=True)[:limits[i]]
            potential_elements.extend(sorted_row)
        # Step 2: Sort combined potential elements in descending order
        potential_elements.sort(reverse=True)
        # Step 3: Sum up top k elements from sorted list to get maximum sum
        return sum(potential_elements[:k])
# @lc code=end