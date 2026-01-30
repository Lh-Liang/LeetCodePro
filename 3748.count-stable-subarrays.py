#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Precompute stable_end array
        stable_end = [0] * n
        current_stable_end = 0
        for i in range(n):
            if i > 0 and nums[i-1] > nums[i]:
                current_stable_end = i
            stable_end[i] = current_stable_end
        
        results = []
        for li, ri in queries:
            count = 0
            for start in range(li, ri + 1):
                end_limit = min(stable_end[start], ri)
                count += (end_limit - start + 1)
            results.append(count)
        return results
# @lc code=end