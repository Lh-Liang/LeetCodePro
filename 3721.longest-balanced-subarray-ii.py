#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        even_set = set()
        odd_set = set()
        count = {}
        for right, num in enumerate(nums):
            if num % 2 == 0:
                even_set.add(num)
            else:
                odd_set.add(num)
            count[num] = count.get(num, 0) + 1
            while left <= right and abs(len(even_set) - len(odd_set)) > 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    if nums[left] % 2 == 0:
                        even_set.remove(nums[left])
                    else:
                        odd_set.remove(nums[left])
                left += 1
            if len(even_set) == len(odd_set):
                max_len = max(max_len, right - left + 1)
        return max_len
# @lc code=end