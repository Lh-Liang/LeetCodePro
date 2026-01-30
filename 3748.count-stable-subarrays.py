#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # next_break[i]: the next index where nums[i] > nums[i+1] (end of current non-decreasing run)
        next_break = [n-1] * n
        end = n-1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                next_break[i] = next_break[i+1]
            else:
                next_break[i] = i
        # precompute number of stable subarrays starting at i
        stable_count = [0] * n
        for i in range(n):
            run_end = next_break[i]
            length = run_end - i + 1
            stable_count[i] = length
        # prefix sum for stable_count
        stable_prefix = [0]*(n+1)
        for i in range(n):
            stable_prefix[i+1] = stable_prefix[i] + stable_count[i]
        ans = []
        for l, r in queries:
            res = 0
            i = l
            while i <= r:
                run_end = min(next_break[i], r)
                length = run_end - i + 1
                res += (length * (length + 1)) // 2
                i = run_end + 1
            ans.append(res)
        return ans
# @lc code=end