#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        start = 0
        max_length = 0
        even_set = set()
        odd_set = set()
        
        for end in range(len(nums)):
            num = nums[end]
            if num % 2 == 0:
                even_set.add(num)
            else:
                odd_set.add(num)
            
            while len(even_set) != len(odd_set):
                start_num = nums[start]
                if start_num % 2 == 0:
                    even_set.discard(start_num)
                else:
                    odd_set.discard(start_num)
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
# @lc code=end