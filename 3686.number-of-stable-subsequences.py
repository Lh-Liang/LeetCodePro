#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp_odd and dp_even track sequences ending in odd and even numbers respectively.
        dp_odd = [0, 0] # [count with one odd, count with two odds]
        dp_even = [0, 0] # [count with one even, count with two evens]
        
        total_stable_subsequences = 0
        
        for num in nums:
            parity = num % 2
            if parity == 1:
                # Transition for odd numbers
                new_dp_odd = [1 + sum(dp_odd), dp_odd[0]] # New single element or extend previous sequence by one odd
                new_dp_even = [sum(dp_even), dp_even[0]]   # Carry over even sequences unchanged
            else:
                # Transition for even numbers
                new_dp_even = [1 + sum(dp_even), dp_even[0]] # New single element or extend previous sequence by one even
                new_dp_odd = [sum(dp_odd), dp_odd[0]]       # Carry over odd sequences unchanged
            
            dp_odd = new_dp_odd[:]
            dp_even = new_dp_even[:]
            
            total_stable_subsequences += (dp_odd[0] + dp_even[0]) % MOD
            total_stable_subsequences %= MOD
        
        return total_stable_subsequences % MOD
# @lc code=end