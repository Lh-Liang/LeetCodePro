#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # Initialize variables
        max_length = 0
        balance_map = {0: -1}  # To handle cases from start
        even_count = 0
        odd_count = 0
        seen_evens = set()
        seen_odds = set()
        
        for i, num in enumerate(nums):
            if num % 2 == 0:
                seen_evens.add(num)
                even_count = len(seen_evens)
            else:
                seen_odds.add(num)
                odd_count = len(seen_odds)
            
            # Calculate current balance state
            current_balance = even_count - odd_count
            
            if current_balance in balance_map:
                # Update max_length if we find a longer balanced subarray
                max_length = max(max_length, i - balance_map[current_balance])
            else:
                # Store first occurrence of this balance state
                balance_map[current_balance] = i
        
        return max_length
# @lc code=end