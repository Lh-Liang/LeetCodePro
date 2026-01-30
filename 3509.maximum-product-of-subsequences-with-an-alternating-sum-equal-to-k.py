#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

from itertools import combinations
from typing import List

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        max_product = -1
        n = len(nums)
        
        # Generate all non-empty subsequences using combinations
        for r in range(1, n + 1):
            for combo in combinations(range(n), r):
                # Calculate alternating sum for this combination
                alt_sum = sum(nums[i] if i % 2 == 0 else -nums[i] for i in combo)
                
                if alt_sum == k:
                    # Calculate product of this subsequence
                    product = 1
                    for i in combo:
                        product *= nums[i]
                        if product > limit:
                            break
                    else:
                        max_product = max(max_product, product)
        
        return max_product if max_product != -1 else -1
# @lc code=end