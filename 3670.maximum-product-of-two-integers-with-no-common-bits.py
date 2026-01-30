#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        from collections import defaultdict
        max_for_mask = defaultdict(int)
        for num in nums:
            if num > max_for_mask[num]:
                max_for_mask[num] = num
        masks = list(max_for_mask.keys())
        ans = 0
        for i in range(len(masks)):
            for j in range(i+1, len(masks)):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, max_for_mask[masks[i]] * max_for_mask[masks[j]])
        return ans
# @lc code=end