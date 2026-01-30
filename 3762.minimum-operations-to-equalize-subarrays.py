#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mapped = [(num % k, num // k) for num in nums]
        # For each residue class mod k, collect indices and quotients
        residue_dict = {}
        for idx, (rem, q) in enumerate(mapped):
            if rem not in residue_dict:
                residue_dict[rem] = []
            residue_dict[rem].append((idx, q))
        # For each residue, store sorted quotients and prefix sums
        precomputed = {}
        for rem in residue_dict:
            arr = sorted(residue_dict[rem], key=lambda x: x[0]) # sort by index
            vals = [q for _, q in arr]
            prefix = [0]
            for v in vals:
                prefix.append(prefix[-1] + v)
            precomputed[rem] = (vals, prefix, [idx for idx, _ in arr])
        results = []
        for li, ri in queries:
            rem = nums[li] % k
            # Check all nums[i] in [li, ri] have same remainder
            ok = True
            for i in range(li, ri+1):
                if nums[i] % k != rem:
                    ok = False
                    break
            if not ok:
                results.append(-1)
                continue
            # Get quotients in [li, ri]
            vals, prefix, indices = precomputed[rem]
            l = bisect.bisect_left(indices, li)
            r = bisect.bisect_right(indices, ri)
            if l == r:
                results.append(0)
                continue
            sub = vals[l:r]
            m = len(sub)
            sub_sorted = sorted(sub)
            median = sub_sorted[m//2]
            # Calculate minimal operations
            ops = sum(abs(x - median) for x in sub_sorted)
            results.append(ops)
        return results
# @lc code=end