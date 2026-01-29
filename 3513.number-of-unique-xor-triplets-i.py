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
        
        # For n >= 3, in a permutation of 1..n, we can always find 
        # i, j, k such that nums[i] ^ nums[j] ^ nums[k] = 0 (e.g., 1^2^3 = 0).
        # The set of values {nums[i] ^ nums[j] ^ nums[k]} will include {1..n} 
        # and 0, plus any other values reachable by XORing three elements.
        # Since we have all numbers 1..n, we can form a basis.
        
        max_val = 0
        for x in nums:
            if x > max_val:
                max_val = x
        
        # Find the smallest 2^k - 1 >= n
        limit = 1
        while limit <= max_val:
            limit <<= 1
        
        return limit
# @lc code=end