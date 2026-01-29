#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        last_pos = {}
        second_last = {}
        for i in range(n):
            num = nums[i]
            if num in last_pos:
                second_last[num] = last_pos[num]
            last_pos[num] = i
        if not second_last:
            return 0
        max_block = max(second_last.values())
        need_start = max_block + 1
        return (need_start + 2) // 3
# @lc code=end