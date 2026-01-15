#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

from typing import List
import heapq

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # Step 1: For each row, sort the elements in descending order.
        # Step 2: From each row, we can take at most limits[i] largest elements.
        # Step 3: Collect all these candidate elements (each row's top limits[i] elements).
        # Step 4: Then we need to select at most k largest elements from these candidates.
        # We can use a min-heap of size k to keep the top k largest elements.
        # Alternatively, we can collect all candidates and sort them in descending order,
        # then take the first k (or less if not enough). Since constraints are up to n*m = 250,000,
        # sorting is O(N log N) which is acceptable.
        candidates = []
        for i, row in enumerate(grid):
            # Sort row in descending order and take the first limits[i] elements.
            sorted_row = sorted(row, reverse=True)
            candidates.extend(sorted_row[:limits[i]])
        # Now sort candidates in descending order.
        candidates.sort(reverse=True)
        # Take the sum of first min(k, len(candidates)) elements.
        return sum(candidates[:k])
# @lc code=end