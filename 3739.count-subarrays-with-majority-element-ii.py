#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        balance = 0
        balance_count = defaultdict(int)
        balance_count[0] = 1
        result = 0
        for num in nums:
            if num == target:
                balance += 1
            else:
                balance -= 1
            result += balance_count[balance - 1]
            balance_count[balance] += 1
        return result
# @lc code=end