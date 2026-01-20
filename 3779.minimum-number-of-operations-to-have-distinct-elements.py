#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        is_distinct = [False] * (n + 1)
        is_distinct[n] = True
        count = {}
        for i in range(n - 1, -1, -1):
            val = nums[i]
            prev_c = count.get(val, 0)
            if prev_c > 0:
                is_distinct[i] = False
            else:
                is_distinct[i] = is_distinct[i + 1]
            count[val] = prev_c + 1
        k = 0
        while True:
            s = min(3 * k, n)
            if is_distinct[s]:
                return k
            k += 1
# @lc code=end