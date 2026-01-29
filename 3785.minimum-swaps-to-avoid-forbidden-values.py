#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        num_cnt = Counter(nums)
        forb_cnt = Counter(forbidden)
        for v, cnt in num_cnt.items():
            if cnt > n - forb_cnt[v]:
                return -1
        bad_cnt = Counter()
        total_bad = 0
        for num, f in zip(nums, forbidden):
            if num == f:
                bad_cnt[num] += 1
                total_bad += 1
        if total_bad == 0:
            return 0
        max_excess = max(2 * c - total_bad for c in bad_cnt.values())
        unmatched = max(total_bad % 2, max_excess)
        return (total_bad - unmatched) // 2 + unmatched
# @lc code=end