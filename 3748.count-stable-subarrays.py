#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        results = []
        for l, r in queries:
            count = 0
            for start in range(l, r + 1):
                min_val = nums[start]
                is_stable = True
                for end in range(start + 1, r + 1):
                    if nums[end] < min_val:
                        is_stable = False
                        break
                    min_val = nums[end]
                if is_stable:
                    count += 1 + (end - start)
            results.append(count)
        return results # @lc code=end