#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Special cases where 0 cannot be formed by XORing 3 distinct elements 
        # from {1, ..., n} or by the property x ^ x ^ x = x.
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, the set {1, 2, ..., n} always contains {1, 2, 3}.
        # Note that 1 ^ 2 ^ 3 = 0. 
        # Once 0 is reachable as a triplet XOR, the set of all possible 
        # triplet XORs (x ^ y ^ z) will cover the entire range [0, 2^m - 1]
        # where 2^m is the smallest power of 2 such that 2^m > n.
        
        # Find the smallest power of 2 greater than n.
        # This can be done by finding the position of the highest set bit.
        m = n.bit_length()
        return 1 << m

# @lc code=end