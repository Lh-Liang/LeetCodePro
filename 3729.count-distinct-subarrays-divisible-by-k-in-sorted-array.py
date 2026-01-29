#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
import math
from collections import Counter
from typing import List

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 1. Total good index-pairs using prefix sums
        prefix_rem = 0
        rem_counts = Counter()
        rem_counts[0] = 1
        total_good_pairs = 0
        
        for x in nums:
            prefix_rem = (prefix_rem + x) % k
            total_good_pairs += rem_counts[prefix_rem]
            rem_counts[prefix_rem] += 1
            
        # 2. Subtract surplus for single-value subarrays to count distinct sequences
        # In a sorted array, only constant-value subarrays can have duplicate sequences.
        surplus = 0
        i = 0
        while i < n:
            val = nums[i]
            j = i
            while j < n and nums[j] == val:
                j += 1
            
            c = j - i
            # Smallest positive integer L0 such that (L0 * val) % k == 0
            # L0 * val = m * k => L0 = lcm(val, k) / val = (val * k / gcd(val, k)) / val
            L0 = k // math.gcd(val, k)
            
            if L0 <= c:
                m_max = c // L0
                # Sum of (c - L) for L = L0, 2*L0, ..., m_max*L0
                # = m_max * c - L0 * (1 + 2 + ... + m_max)
                current_surplus = m_max * c - L0 * (m_max * (m_max + 1) // 2)
                surplus += current_surplus
            
            i = j
            
        return total_good_pairs - surplus
# @lc code=end