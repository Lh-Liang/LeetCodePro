#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        # Initialize variables for simulation
        start = 1  # start of our current sequence
        step = 1   # step size between elements in our current sequence
        remaining = n  # number of elements currently remaining
        left_to_right = True  # direction of elimination
        
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                # If we're eliminating from left or if odd count when eliminating from right, adjust start
                start += step
            # Each round reduces the array by half (approximately)
            remaining //= 2
            step *= 2  # step doubles for each round (as we're effectively skipping every other element)
            left_to_right = not left_to_right  # toggle direction
        
        return start
# @lc code=end