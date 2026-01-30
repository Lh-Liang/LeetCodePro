#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        
        def dfs(index, a_xor, b_and, c_xor):
            nonlocal max_val
            if index == n:
                max_val = max(max_val, a_xor + b_and + c_xor)
                return
            # Option 1: Add nums[index] to A
            dfs(index + 1, a_xor ^ nums[index], b_and, c_xor)
            # Option 2: Add nums[index] to B
            dfs(index + 1, a_xor, b_and & nums[index] if b_and != 0 else nums[index], c_xor)
            # Option 3: Add nums[index] to C
            dfs(index + 1, a_xor, b_and, c_xor ^ nums[index])
        
        dfs(0, 0, 0xFFFFFFFFFF, 0) # Start with full range for AND operation in B
        return max_val
# @lc code=end