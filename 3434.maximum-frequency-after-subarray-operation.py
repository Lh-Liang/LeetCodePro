#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total_k = nums.count(k)
        ans = total_k
        for orig in range(1, 51):
            curr = 0
            max_sum = 0
            for num in nums:
                val = (1 if num == orig else 0) - (1 if num == k else 0)
                curr += val
                if curr < 0:
                    curr = 0
                max_sum = max(max_sum, curr)
            ans = max(ans, total_k + max_sum)
        return ans

# @lc code=end