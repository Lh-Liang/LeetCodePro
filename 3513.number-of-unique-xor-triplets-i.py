#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, the set of unique XOR triplet values covers the entire range
        # of the XOR span of integers [1, n]. This span is always [0, 2^k - 1]
        # where k is the bit length of n.
        return 1 << n.bit_length()
# @lc code=end