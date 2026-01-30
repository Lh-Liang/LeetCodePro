#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_xors = set()
        n = len(nums)
        for i in range(n):
            xor_value = 0
            for j in range(i, n):
                xor_value ^= nums[j]
                unique_xors.add(xor_value)
        return len(unique_xors)
# @lc code=end