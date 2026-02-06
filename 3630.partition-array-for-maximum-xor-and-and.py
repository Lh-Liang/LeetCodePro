#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        max_result = 0
        for i in range(1 << n):
            A, B, C = [], [], []
            for j in range(n):
                if i & (1 << j):
                    A.append(nums[j])
                elif (i >> j) & 1 == 0:
                    B.append(nums[j])
                else:
                    C.append(nums[j])
            xor_A = 0 if not A else reduce(lambda x, y: x ^ y, A)
            and_B = (1 << 32) - 1 if not B else reduce(lambda x, y: x & y, B)
            xor_C = 0 if not C else reduce(lambda x, y: x ^ y, C)
            max_result = max(max_result, xor_A + and_B + xor_C)
        return max_result # @lc code=end