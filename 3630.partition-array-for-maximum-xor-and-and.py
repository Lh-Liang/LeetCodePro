#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        from itertools import combinations
        n = len(nums)
        max_value = 0
        # Try all combinations for partitioning into 3 groups
        for i in range(n+1):
            for j in range(i, n+1):
                A = nums[:i]
                B = nums[i:j]
                C = nums[j:]
                # Calculate XOR(A), AND(B), XOR(C)
                xor_a = self.calculate_xor(A) if A else 0
                and_b = self.calculate_and(B) if B else 0
                xor_c = self.calculate_xor(C) if C else 0
                max_value = max(max_value, xor_a + and_b + xor_c)
        return max_value
    
    def calculate_xor(self, arr: List[int]) -> int:
        result = 0
        for num in arr:
            result ^= num
        return result
    
    def calculate_and(self, arr: List[int]) -> int:
        if not arr: return 0
        result = arr[0]
        for num in arr[1:]:
            result &= num
        return result
# @lc code=end