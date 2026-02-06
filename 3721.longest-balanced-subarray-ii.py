#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # HashMap to store first occurrence of balance
        balance_map = {0: -1}
        # Sets to track distinct evens and odds
        even_set = set()
        odd_set = set()
        max_length = 0
        balance = 0  # Difference between counts of evens and odds
        for i, num in enumerate(nums):
            if num % 2 == 0:
                even_set.add(num)
            else:
                odd_set.add(num)
            # Calculate balance as difference between sizes of sets
            balance = len(even_set) - len(odd_set)
            if balance in balance_map:
                max_length = max(max_length, i - balance_map[balance])
            else:
                balance_map[balance] = i  # Store first occurrence of this balance
        return max_length
# @lc code=end