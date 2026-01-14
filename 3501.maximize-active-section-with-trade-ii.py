#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
from bisect import bisect_left, bisect_right
from typing import List
from math import log2

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Parse into runs: (start, length, char)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append([i, j - i])  # start, length
            i = j
        m = len(runs)
        
        # Prefix sum for '1's
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '1' else 0)
        
        total_ones = prefix[n]
        
        # For '0' runs, compute gains (sum of adjacent '0' runs if merged over a '1' run)
        # gains[i] = len(zero_run_i) + len(zero_run_{i+1}) where they're consecutive '0' runs
        zero_runs = []  # (run_index, start, length)
        for i in range(m):
            if s[runs[i][0]] == '0':
                zero_runs.append((i, runs[i][0], runs[i][1]))
        
        num_zeros = len(zero_runs)
        
        # Pairs of consecutive '0' runs
        pairs = []  # (left_zero_start, right_zero_end, gain, left_run_idx, right_run_idx)
        for i in range(num_zeros - 1):
            li, ls, ll = zero_runs[i]
            ri, rs, rl = zero_runs[i + 1]
            if ri == li + 2:  # There's exactly one '1' run between them
                pairs.append((ls, rs + rl - 1, ll + rl, i, i + 1))
        
        num_pairs = len(pairs)
        
        if num_pairs == 0:
            return [prefix[r+1] - prefix[l] for l, r in queries]
        
        # Build sparse table for range max
        LOG = max(1, int(log2(num_pairs)) + 2)
        sparse = [[0] * num_pairs for _ in range(LOG)]
        
        for i in range(num_pairs):
            sparse[0][i] = pairs[i][2]
        
        for j in range(1, LOG):
            for i in range(num_pairs - (1 << j) + 1):
                sparse[j][i] = max(sparse[j-1][i], sparse[j-1][i + (1 << (j-1))])
        
        def range_max(l, r):
            if l > r:
                return 0
            k = int(log2(r - l + 1))
            return max(sparse[k][l], sparse[k][r - (1 << k) + 1])
        
        # Precompute pair boundaries
        pair_left = [p[0] for p in pairs]
        pair_right = [p[1] for p in pairs]
        
        results = []
        for l, r in queries:
            base = prefix[r+1] - prefix[l]
            
            # Find pairs fully inside [l, r]
            lo = bisect_left(pair_left, l)
            hi = bisect_right(pair_right, r) - 1
            
            max_gain = 0
            if lo <= hi:
                max_gain = range_max(lo, hi)
            
            # Handle boundary pairs (clipped)
            if lo > 0:
                idx = lo - 1
                if pair_right[idx] <= r:
                    li = pairs[idx][3]
                    ri = pairs[idx][4]
                    ls, ll = zero_runs[li][1], zero_runs[li][2]
                    rs, rl = zero_runs[ri][1], zero_runs[ri][2]
                    left_clip = max(0, min(ls + ll - 1, r) - max(ls, l) + 1)
                    right_clip = max(0, min(rs + rl - 1, r) - max(rs, l) + 1)
                    max_gain = max(max_gain, left_clip + right_clip)
            
            if hi < num_pairs - 1:
                idx = hi + 1
                if pair_left[idx] >= l:
                    li = pairs[idx][3]
                    ri = pairs[idx][4]
                    ls, ll = zero_runs[li][1], zero_runs[li][2]
                    rs, rl = zero_runs[ri][1], zero_runs[ri][2]
                    left_clip = max(0, min(ls + ll - 1, r) - max(ls, l) + 1)
                    right_clip = max(0, min(rs + rl - 1, r) - max(rs, l) + 1)
                    max_gain = max(max_gain, left_clip + right_clip)
            
            results.append(base + max_gain)
        
        return results
# @lc code=end