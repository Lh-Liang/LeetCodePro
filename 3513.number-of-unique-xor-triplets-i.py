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
                current_xor = nums[i]
                for k in range(j, n):
                    current_xor ^= nums[k]
                    unique_xor_values.add(current_xor)
        return len(unique_xor_values)
# @lc code=end