#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        from collections import defaultdict
        # Map mask to list of numbers (descending order)
        mask_to_nums = defaultdict(list)
        for num in nums:
            mask = num
            mask_to_nums[mask].append(num)
        # For each mask, keep top two largest numbers (to handle duplicate masks)
        for mask in mask_to_nums:
            mask_to_nums[mask].sort(reverse=True)
            if len(mask_to_nums[mask]) > 2:
                mask_to_nums[mask] = mask_to_nums[mask][:2]
        masks = list(mask_to_nums.keys())
        max_prod = 0
        # Check all pairs of masks
        n = len(masks)
        for i in range(n):
            m1 = masks[i]
            nums1 = mask_to_nums[m1]
            # Case 1: Same mask, need two different occurrences
            if len(nums1) >= 2 and (m1 & m1) == 0:
                prod = nums1[0] * nums1[1]
                max_prod = max(max_prod, prod)
            # Case 2: Different masks
            for j in range(i + 1, n):
                m2 = masks[j]
                if m1 & m2 == 0:
                    prod = nums1[0] * mask_to_nums[m2][0]
                    max_prod = max(max_prod, prod)
        return max_prod
# @lc code=end