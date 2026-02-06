#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        results = []
        for li, ri in queries:
            count = 0
            left = li
            while left <= ri:
                right = left + 1
                # Find end of current stable segment
                while right <= ri and nums[right] >= nums[right - 1]:
                    right += 1
                # Calculate number of stable subarrays within [left, right-1]
                n = right - left
                count += n * (n + 1) // 2
                # Move left pointer to start of next potential segment
                left = right
            results.append(count)
        return results
# @lc code=end