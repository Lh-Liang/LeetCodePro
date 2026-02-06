#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        count = 0
        balance = 0
        previous_balances = defaultdict(int)
        previous_balances[0] = 1 # Base case for subarray starting at index 0
        
        for num in nums:
            if num == target:
                balance += 1
            else:
                balance -= 1
            
            # Check how many times (balance - 1) has been seen before for majority condition
            count += previous_balances[balance - 1]
            
            # Record current balance state for future indices
            previous_balances[balance] += 1
        
        return count
# @lc code=end