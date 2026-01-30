#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        for a, b in swaps:
            union(a, b)
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        res = [0]*n
        for idxs in groups.values():
            vals = sorted([nums[i] for i in idxs], reverse=True)
            even_idxs = sorted([i for i in idxs if i % 2 == 0])
            odd_idxs = sorted([i for i in idxs if i % 2 == 1])
            # Try both assignments and pick the best
            max_group_sum = float('-inf')
            for assign_largest_to_even in [True, False]:
                temp = [0]*len(idxs)
                if assign_largest_to_even:
                    evens, odds = even_idxs, odd_idxs
                else:
                    evens, odds = odd_idxs, even_idxs
                ct_evens = len(evens)
                ct_odds = len(odds)
                sorted_evens = vals[:ct_evens]
                sorted_odds = vals[ct_evens:]
                temp_assign = {}
                for i, v in zip(evens, sorted_evens):
                    temp_assign[i] = v
                for i, v in zip(odds, sorted(sorted_odds)):
                    temp_assign[i] = v
                # Compute group alternating sum
                group_sum = 0
                for i in idxs:
                    if i % 2 == 0:
                        group_sum += temp_assign[i]
                    else:
                        group_sum -= temp_assign[i]
                max_group_sum = max(max_group_sum, group_sum)
                # Save assignment if it's the best
                if max_group_sum == group_sum:
                    best_assign = temp_assign
            for i in idxs:
                res[i] = best_assign[i]
        alt_sum = 0
        for i, v in enumerate(res):
            if i % 2 == 0:
                alt_sum += v
            else:
                alt_sum -= v
        return alt_sum
# @lc code=end