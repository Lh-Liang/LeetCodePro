#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]
        unique_xor_values = set()
        for start in range(n):
            for end in range(start, n):
                xor_value = prefix_xor[end + 1] ^ prefix_xor[start]
                unique_xor_values.add(xor_value)
        return len(unique_xor_values)
# @lc code=end