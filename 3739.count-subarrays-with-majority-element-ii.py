#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            freq = 0
            total = 0
            for j in range(i, n):
                if nums[j] == target:
                    freq += 1
                total += 1
                if freq > total / 2:
                    count += 1
        return count
# @lc code=end