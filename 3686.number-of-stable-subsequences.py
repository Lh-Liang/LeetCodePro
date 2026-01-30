#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#
# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        count_odd, count_even = 0, 0
        last_parity = None
        streak = 0
        for num in nums:
            current_parity = num % 2
            if current_parity == last_parity:
                streak += 1
            else:
                streak = 1
                last_parity = current_parity
            if streak < 3:
                if current_parity == 0: # Even number
                    count_even = (count_even + count_odd + 1) % mod
                else: # Odd number
                    count_odd = (count_odd + count_even + 1) % mod
        return (count_odd + count_even) % mod # Total stable subsequences modulo mod
# @lc code=end