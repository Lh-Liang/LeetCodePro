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
        def dfs(i, xor_a, and_b, xor_c, has_b):
            nonlocal max_val
            if i == n:
                # If B is empty, AND(B) is 0 (by problem statement)
                b_val = and_b if has_b else 0
                max_val = max(max_val, xor_a + b_val + xor_c)
                return
            # Place nums[i] in A
            dfs(i+1, xor_a ^ nums[i], and_b, xor_c, has_b)
            # Place nums[i] in B
            dfs(i+1, xor_a, nums[i] if not has_b else (and_b & nums[i]), xor_c, True)
            # Place nums[i] in C
            dfs(i+1, xor_a, and_b, xor_c ^ nums[i], has_b)
        dfs(0, 0, 0, 0, False)
        return max_val
# @lc code=end