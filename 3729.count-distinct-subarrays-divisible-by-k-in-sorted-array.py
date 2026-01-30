# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        prefix_sums = {0: -1}  # Maps sum mod k to index
        count = 0
        for i in range(n):
            prefix_sum += nums[i]
            mod = prefix_sum % k
            if mod in prefix_sums:
                if prefix_sums[mod] < i - 1:  # Ensure distinctness by checking the range
                    count += 1 
            else:
                prefix_sums[mod] = i  # Store first occurrence only for distinctness
        return count
# @lc code=end