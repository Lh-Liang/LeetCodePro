#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        res = []
        nums = nums[:]  # Make a copy for in-place modification
        for idx, val, start, x in queries:
            nums[idx] = val
            subarr = nums[start:]
            m = len(subarr)
            suffix_prod = [1] * (m + 1)
            for i in range(m - 1, -1, -1):
                suffix_prod[i] = (suffix_prod[i + 1] * subarr[i]) % k
            count = 0
            # For each possible suffix removal (including removing nothing)
            for j in range(m):  # Remove suffix starts at j (i.e., keep subarr[:j])
                prod = suffix_prod[0]  # full product
                if j == 0:
                    prod = suffix_prod[0]
                else:
                    prod = suffix_prod[0] * pow(suffix_prod[j], -1, k) % k
                if prod == x:
                    count += 1
            if suffix_prod[0] == x:  # Case when removing nothing
                count += 1
            res.append(count)
        return res
# @lc code=end