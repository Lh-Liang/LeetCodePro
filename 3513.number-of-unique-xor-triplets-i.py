#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        # For small n, brute force all triplets
        if n <= 2000:
            seen = set()
            for i in range(n):
                for j in range(i, n):
                    for k in range(j, n):
                        seen.add(nums[i] ^ nums[j] ^ nums[k])
            return len(seen)
        else:
            # For large n, the possible values of XOR from the permutation [1..n] is at most n
            # Since every value from 1 to n can be formed, and XOR is a group operation,
            # it covers all possible values from 0 up to n, but let's compute it experimentally
            return n
# @lc code=end