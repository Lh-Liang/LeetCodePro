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
        
        # For n >= 3, the unique XOR values form the set {0, 1, ..., 2^k - 1}
        # where 2^k is the smallest power of 2 strictly greater than n.
        # This is because {1, 2, 3} is in the set, so 1^2^3 = 0 is a reachable XOR value.
        # Once 0 is reachable, and the set contains a basis for [1, n],
        # the XOR triplets can generate the entire span.
        
        p = 1
        while p <= n:
            p <<= 1
        return p
# @lc code=end