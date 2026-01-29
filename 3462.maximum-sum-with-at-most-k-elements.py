#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        all_candidates = []
        
        # Step 1: Extract the best possible candidates from each row
        for i in range(len(grid)):
            # Only sort and take elements if the limit for this row is > 0
            if limits[i] > 0:
                row_sorted = sorted(grid[i], reverse=True)
                all_candidates.extend(row_sorted[:limits[i]])
        
        # Step 2: Sort all valid candidates globally
        all_candidates.sort(reverse=True)
        
        # Step 3: Sum the top k elements. Since elements are non-negative, 
        # we take as many as possible up to k.
        return sum(all_candidates[:k])
# @lc code=end