#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def count_stable_in_range(l, r):
            count = 0
            start = l
            while start <= r:
                end = start
                while end < r and nums[end] <= nums[end + 1]:
                    end += 1
                # Calculate number of stable subarrays in this range [start, end]
                length = end - start + 1
                count += (length * (length + 1)) // 2 # Sum of first n natural numbers formula for counting subarrays
                start = end + 1 # Move start to next potential starting point
            return count
        
        results = []
        for li, ri in queries:
            results.append(count_stable_in_range(li, ri))
        return results
# @lc code=end