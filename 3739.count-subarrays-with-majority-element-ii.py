#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0
        balance = 0
        balance_count = defaultdict(int)
        balance_count[0] = 1 # To handle entire prefix being valid directly
        
        for num in nums:
            if num == target:
                balance += 1
            else:
                balance -= 1
            
            # Check how many times we have seen this balance before (indicating possible majority subarray)
            count += balance_count[balance - 1]
            
            # Record current balance in hashmap
            balance_count[balance] += 1
        
        return count
# @lc code=end