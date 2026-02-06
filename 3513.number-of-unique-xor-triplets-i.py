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
            for j in range(i, n):
                for k in range(j, n):
                    xor_value = nums[i] ^ nums[j] ^ nums[k]
                    unique_xor_values.add(xor_value)
        return len(unique_xor_values)
# @lc code=end