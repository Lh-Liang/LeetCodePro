#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        start = 0
        max_len = 0
        even_count = defaultdict(int)  # Tracks occurrences of each even number
        odd_count = defaultdict(int)   # Tracks occurrences of each odd number
        evens = odds = 0              # Distinct even and odd counts
        
        def update_counts(num, increment=True):
            nonlocal evens, odds  # Ensure these are updated correctly in scope
            if num % 2 == 0:
                if increment:
                    if even_count[num] == 0:
                        evens += 1
                    even_count[num] += 1
                else:
                    if even_count[num] == 1:
                        evens -= 1
                    even_count[num] -= 1
            else:
                if increment:
                    if odd_count[num] == 0:
                        odds += 1
                    odd_count[num] += 1
                else:
                    if odd_count[num] == 1:
                        odds -= 1
                    odd_count[num] -= 1
        
        for end in range(len(nums)):
            update_counts(nums[end], increment=True)
            
            # Adjust 'start' to maintain balance condition (evens == odds)
            while start <= end and evens != odds:
                update_counts(nums[start], increment=False)
                start += 1
            
            # Check for balanced subarray length update after adjustment
            if evens == odds:
                max_len = max(max_len, end - start + 1)
        
        return max_len
# @lc code=end