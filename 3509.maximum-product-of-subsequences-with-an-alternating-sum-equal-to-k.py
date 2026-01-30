#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        from collections import defaultdict
        n = len(nums)
        # dp[(alt_sum, parity)] = max_product
        dp = defaultdict(int)
        res = -1
        for i, num in enumerate(nums):
            next_dp = dp.copy()
            # Start new subsequence at index i
            alt_sum = num
            parity = 0  # first element is at even index in subsequence
            prod = num
            if prod <= limit:
                next_dp[(alt_sum, parity)] = max(next_dp.get((alt_sum, parity), 0), prod)
                if alt_sum == k:
                    res = max(res, prod)
            # Extend all existing subsequences by including nums[i]
            for (old_alt, old_parity), old_prod in dp.items():
                new_parity = old_parity ^ 1  # flip parity when adding an element
                new_alt = old_alt + num if old_parity == 0 else old_alt - num
                new_prod = old_prod * num
                if new_prod <= limit:
                    if next_dp[(new_alt, new_parity)] < new_prod:
                        next_dp[(new_alt, new_parity)] = new_prod
                        if new_alt == k:
                            res = max(res, new_prod)
            dp = next_dp
        return res
# @lc code=end