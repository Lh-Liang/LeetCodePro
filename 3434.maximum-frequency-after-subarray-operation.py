#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        from collections import Counter
        n = len(nums)
        max_freq = 0
        # Count how many nums are already k
        count_k = sum(1 for num in nums if num == k)
        for d in range(-49, 50):
            target = [1 if k - num == d else 0 for num in nums]
            # Find the longest contiguous segment where value is 1
            curr = best = 0
            for val in target:
                if val == 1:
                    curr += 1
                    best = max(best, curr)
                else:
                    curr = 0
            # After applying this operation, frequency of k is best + (count_k if best == 0 else 0)
            # Actually, the operation replaces those elements, so 'best' is the count from that subarray,
            # and outside the subarray, only the elements already equal to k remain.
            # But since the operation can be anywhere, and we can pick the segment with the most replacements,
            # So for each d, max freq is max(best, count_k)
            max_freq = max(max_freq, best)
        # Also consider the case where we don't do any operation: count_k
        max_freq = max(max_freq, count_k)
        return max_freq
# @lc code=end