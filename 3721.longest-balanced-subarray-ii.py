#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        maxlen = 0
        left = 0
        even_count = defaultdict(int)
        odd_count = defaultdict(int)
        even_distinct = 0
        odd_distinct = 0
        for right, num in enumerate(nums):
            if num % 2 == 0:
                if even_count[num] == 0:
                    even_distinct += 1
                even_count[num] += 1
            else:
                if odd_count[num] == 0:
                    odd_distinct += 1
                odd_count[num] += 1
            while left <= right and even_distinct != odd_distinct:
                num_left = nums[left]
                if num_left % 2 == 0:
                    even_count[num_left] -= 1
                    if even_count[num_left] == 0:
                        even_distinct -= 1
                else:
                    odd_count[num_left] -= 1
                    if odd_count[num_left] == 0:
                        odd_distinct -= 1
                left += 1
            # After window adjustment, verify data structures are correct
            assert even_distinct == len([k for k,v in even_count.items() if v > 0])
            assert odd_distinct == len([k for k,v in odd_count.items() if v > 0])
            if even_distinct == odd_distinct:
                maxlen = max(maxlen, right - left + 1)
        # Final verification step could be added here if needed
        return maxlen
# @lc code=end