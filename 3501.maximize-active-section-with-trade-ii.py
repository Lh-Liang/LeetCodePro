#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

import math

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + (1 if s[i] == '1' else 0)
            
        def get_ones(l, r):
            return pref[r+1] - pref[l]

        zero_blocks = []
        one_blocks = []
        
        i = 0
        while i < n:
            start = i
            val = s[i]
            while i < n and s[i] == val:
                i += 1
            if val == '0':
                zero_blocks.append((start, i - 1))
            else:
                one_blocks.append((start, i - 1))

        m0 = len(zero_blocks)
        m1 = len(one_blocks)
        
        # Sparse Table for Max Zero Block Length
        # A zero block in s[l...r] is surrounded by 1s if it's not the first/last block in augmented string
        # In augmented string 1 + s[l...r] + 1, any block of 0s in s[l...r] is surrounded by 1s (or boundary 1s)
        st_max_z = []
        if m0 > 0:
            k = int(math.log2(m0)) + 1
            st_max_z = [[0] * k for _ in range(m0)]
            for i in range(m0):
                st_max_z[i][0] = zero_blocks[i][1] - zero_blocks[i][0] + 1
            for j in range(1, k):
                for i in range(m0 - (1 << j) + 1):
                    st_max_z[i][j] = max(st_max_z[i][j-1], st_max_z[i + (1 << (j-1))][j-1])

        def query_max_z(L, R):
            if L > R: return -float('inf')
            j = int(math.log2(R - L + 1))
            return max(st_max_z[L][j], st_max_z[R - (1 << j) + 1][j])

        # Sparse Table for Min One Block Length
        # A one block is surrounded by 0s if it's not the first or last block of the original s,
        # and within the range [l, r], it must not touch the boundaries if those boundaries are effectively 1s.
        st_min_o = []
        valid_one_indices = []
        for idx, (start, end) in enumerate(one_blocks):
            if start > 0 and end < n - 1 and s[start-1] == '0' and s[end+1] == '0':
                valid_one_indices.append(idx)
        
        m1_v = len(valid_one_indices)
        if m1_v > 0:
            k = int(math.log2(m1_v)) + 1
            st_min_o = [[0] * k for _ in range(m1_v)]
            for i in range(m1_v):
                idx = valid_one_indices[i]
                st_min_o[i][0] = one_blocks[idx][1] - one_blocks[idx][0] + 1
            for j in range(1, k):
                for i in range(m1_v - (1 << j) + 1):
                    st_min_o[i][j] = min(st_min_o[i][j-1], st_min_o[i + (1 << (j-1))][j-1])

        def query_min_o(L, R):
            if L > R: return float('inf')
            j = int(math.log2(R - L + 1))
            return min(st_min_o[L][j], st_min_o[R - (1 << j) + 1][j])

        import bisect
        ans = []
        z_starts = [b[0] for b in zero_blocks]
        o_v_starts = [one_blocks[idx][0] for idx in valid_one_indices]

        for l, r in queries:
            initial_ones = get_ones(l, r)
            
            # Find zero blocks fully contained in [l, r]
            idx_z_start = bisect.bisect_left(z_starts, l)
            idx_z_end = bisect.bisect_right(z_starts, r)
            max_z = -float('inf')
            if idx_z_start < idx_z_end:
                # Check if block is fully contained
                actual_end = idx_z_end - 1
                while actual_end >= idx_z_start and zero_blocks[actual_end][1] > r:
                    actual_end -= 1
                if idx_z_start <= actual_end:
                    max_z = query_max_z(idx_z_start, actual_end)
            
            # Find valid one blocks fully contained in [l, r]
            idx_o_start = bisect.bisect_left(o_v_starts, l)
            idx_o_end = bisect.bisect_right(o_v_starts, r)
            min_o = float('inf')
            if idx_o_start < idx_o_end:
                actual_end = idx_o_end - 1
                while actual_end >= idx_o_start and one_blocks[valid_one_indices[actual_end]][1] > r:
                    actual_end -= 1
                if idx_o_start <= actual_end:
                    min_o = query_min_o(idx_o_start, actual_end)
            
            if max_z != -float('inf') and min_o != float('inf'):
                ans.append(max(initial_ones, initial_ones + max_z - min_o))
            else:
                ans.append(initial_ones)
        return ans