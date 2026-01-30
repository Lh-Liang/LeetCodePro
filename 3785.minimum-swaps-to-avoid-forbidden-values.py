#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        from collections import defaultdict, Counter
        n = len(nums)
        conflict = [] # indices where nums[i] == forbidden[i]
        count_nums = Counter(nums)
        count_forbidden = Counter(forbidden)
        # Step 1: Find conflict positions
        for i in range(n):
            if nums[i] == forbidden[i]:
                conflict.append(i)
        if not conflict:
            return 0
        # If there are too many of one value, it may be impossible
        # Check if for any value, count in nums > n - count in forbidden[value]
        # because we can't move all of them away from their forbidden positions
        for v in count_nums:
            bad = 0
            for i in range(n):
                if forbidden[i] == v and nums[i] == v:
                    bad += 1
            if bad > n - count_forbidden[v]:
                return -1
        # Now, try to resolve conflicts by swapping
        # Each swap can resolve at most 2 conflicts
        total_conflicts = len(conflict)
        # Count the number of conflicts for each value
        conflict_val = Counter([nums[i] for i in conflict])
        # The minimal number of swaps is ceil(total_conflicts / 2), but
        # in some cases, we cannot resolve all with pairwise swaps (odd cycles),
        # so we need to check for the worst-case value
        max_val_conflict = max(conflict_val.values())
        min_swaps = max((total_conflicts + 1) // 2, max_val_conflict)
        return min_swaps
# @lc code=end