#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_xor_values = set()
        n = len(nums)
        for i in range(n):
            xor_sum = 0
            for j in range(i, n):
                xor_sum ^= nums[j]
                # Every (i, j, k) where i <= j <= k gives the same result as (i, j)
                unique_xor_values.add(xor_sum)
        return len(unique_xor_values)
# @lc code=end