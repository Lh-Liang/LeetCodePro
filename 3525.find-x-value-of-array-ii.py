#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        results = []
        for indexi, valuei, starti, xi in queries:
            # Update nums with new value at indexi
            nums[indexi] = valuei
            # Calculate x-value for current query using modular arithmetic
            count = 0
            product_mod_k = 1
            for j in range(starti, len(nums)):
                product_mod_k = (product_mod_k * nums[j]) % k
                if product_mod_k == xi:
                    count += 1
            results.append(count)
        return results
# @lc code=end