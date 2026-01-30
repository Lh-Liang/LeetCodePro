#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        from heapq import nlargest
        # Step 1: Select elements according to limits from each row
        selected_elements = []
        for i in range(len(grid)):
            # Sort current row in descending order and take up to limits[i] elements
            selected_elements.extend(sorted(grid[i], reverse=True)[:limits[i]])
        
        # Step 2: Select top k elements from combined selection
        return sum(nlargest(k, selected_elements))
# @lc code=end