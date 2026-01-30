#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
from typing import List
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # Efficiently handle multiple queries with updates and repeated computations
        res = []
        n = len(nums)
        nums = nums[:]
        for index, value, start, xi in queries:
            nums[index] = value
            count = 0
            # Precompute prefix products modulo k for nums[start:]
            prefix_prod = [1]
            for i in range(start, n):
                prefix_prod.append((prefix_prod[-1] * nums[i]) % k)
            for end in range(1, n - start + 1):
                if prefix_prod[end] == xi:
                    count += 1
            res.append(count)
        return res
# @lc code=end