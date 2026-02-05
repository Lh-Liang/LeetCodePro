# @lc app=leetcode id=3630 lang=python3
# [3630] Partition Array for Maximum XOR and AND

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        from functools import lru_cache
        
        n = len(nums)
        
        # Use lru_cache for memoization
        @lru_cache(None)
        def dfs(index: int, xorA: int, andB: int, xorC: int) -> int:
            if index == n:
                return xorA + andB + xorC
            
            current_num = nums[index]
            # Option 1: Add current_num to A (XOR)
            option1 = dfs(index + 1, xorA ^ current_num, andB, xorC)
            # Option 2: Add current_num to B (AND)
            option2 = dfs(index + 1, xorA, andB & current_num if andB else current_num, xorC)
            # Option 3: Add current_num to C (XOR)
            option3 = dfs(index + 1, xorA, andB, xorC ^ current_num)
            
            return max(option1, option2, option3)
        
        return dfs(0, 0, 0xfffffffff if nums else 0x0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f , 0) # Assume initial AND as all bits set for correct bitwise operation on first element.
# @lc code=end