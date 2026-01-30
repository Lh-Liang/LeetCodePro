#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        even_set = set()
        odd_set = set()
        
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                even_set.add(nums[right])
            else:
                odd_set.add(nums[right])
                
            while len(even_set) != len(odd_set) and left <= right:
                if nums[left] % 2 == 0:
                    even_set.remove(nums[left])
                else:
                    odd_set.remove(nums[left])
                left += 1
            
            if len(even_set) == len(odd_set):
                max_length = max(max_length, right - left + 1)
        return max_length
# @lc code=end