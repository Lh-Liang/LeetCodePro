#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Step 1: Create a list of tuples (num, bitmask)
        num_bitmasks = [(num, self.calculate_bitmask(num)) for num in nums]
        # Step 2: Sort by number in descending order to maximize product early
        num_bitmasks.sort(reverse=True, key=lambda x: x[0])
        max_product = 0
        n = len(num_bitmasks)
        # Step 3: Check pairs for no common bits and calculate product
        for i in range(n):
            for j in range(i + 1, n):
                if num_bitmasks[i][1] & num_bitmasks[j][1] == 0:  # No common set bits
                    max_product = max(max_product, num_bitmasks[i][0] * num_bitmasks[j][0])
        return max_product
    
    def calculate_bitmask(self, num):
        """Calculate the bitmask representation of a number."""
        bitmask = 0
        shift = 0
        while num > 0:
            if num & 1:
                bitmask |= (1 << shift)
            shift += 1
            num >>= 1
        return bitmask
# @lc code=end