#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Step 1: Preprocess non-decreasing segments
        seg_start = [0] * n  # seg_start[i]: start index of non-decreasing segment containing i
        l = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                l = i
            seg_start[i] = l

        res = []
        for li, ri in queries:
            ans = 0
            i = li
            while i <= ri:
                # Find the start of the non-decreasing segment
                seg_l = seg_start[i]
                # Find the rightmost index in the same segment within the query
                j = i
                while j+1 <= ri and seg_start[j+1] == seg_l:
                    j += 1
                length = j - i + 1
                # Count all stable subarrays in this segment within the query
                ans += length * (length + 1) // 2
                i = j + 1
            # Step 6: After processing, answer should reflect all stable subarrays in [li, ri]
            res.append(ans)
        return res
# @lc code=end