#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # max_reach[i] = the maximum index j such that nums[i:j+1] is non-decreasing
        max_reach = [0] * n
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                max_reach[i] = i
            elif nums[i + 1] < nums[i]:
                max_reach[i] = i
            else:
                max_reach[i] = max_reach[i + 1]
        
        result = []
        for l, r in queries:
            count = 0
            for i in range(l, r + 1):
                # The maximum ending position within [l, r]
                end = min(max_reach[i], r)
                # Number of stable subarrays starting at i
                count += (end - i + 1)
            
            result.append(count)
        
        return result
# @lc code=end