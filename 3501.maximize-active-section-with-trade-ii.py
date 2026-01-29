#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        import math

        n = len(s)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + (1 if s[i] == '1' else 0)
            
        ones_blocks = []
        zeros_blocks = []
        
        i = 0
        while i < n:
            start = i
            char = s[i]
            while i < n and s[i] == char:
                i += 1
            if char == '1':
                ones_blocks.append((start, i - 1, i - start))
            else:
                zeros_blocks.append((start, i - 1, i - start))

        # Sparse Table for Max Zeros
        num_z = len(zeros_blocks)
        if num_z > 0:
            max_log_z = num_z.bit_length()
            st_max_z = [[0] * num_z for _ in range(max_log_z)]
            for j in range(num_z):
                st_max_z[0][j] = zeros_blocks[j][2]
            for i in range(1, max_log_z):
                for j in range(num_z - (1 << i) + 1):
                    st_max_z[i][j] = max(st_max_z[i-1][j], st_max_z[i-1][j + (1 << (i-1))])

        def query_max_z(L, R):
            if L > R: return 0
            i = (R - L + 1).bit_length() - 1
            return max(st_max_z[i][L], st_max_z[i][R - (1 << i) + 1])

        # Sparse Table for Min Ones
        num_o = len(ones_blocks)
        if num_o > 0:
            max_log_o = num_o.bit_length()
            st_min_o = [[float('inf')] * num_o for _ in range(max_log_o)]
            for j in range(num_o):
                # A '1' block is tradeable only if surrounded by '0's
                # This means it cannot be the very first or very last block of the string s
                # unless we check the query boundaries. Actually, a '1' block is tradeable
                # within s[li...ri] if s[start-1] == '0' and s[end+1] == '0'.
                if ones_blocks[j][0] > 0 and ones_blocks[j][1] < n - 1 and s[ones_blocks[j][0]-1] == '0' and s[ones_blocks[j][1]+1] == '0':
                    st_min_o[0][j] = ones_blocks[j][2]
            for i in range(1, max_log_o):
                for j in range(num_o - (1 << i) + 1):
                    st_min_o[i][j] = min(st_min_o[i-1][j], st_min_o[i-1][j + (1 << (i-1))])

        def query_min_o(L, R):
            if L > R: return float('inf')
            i = (R - L + 1).bit_length() - 1
            return min(st_min_o[i][L], st_min_o[i][R - (1 << i) + 1])

        from bisect import bisect_left, bisect_right
        o_starts = [b[0] for b in ones_blocks]
        o_ends = [b[1] for b in ones_blocks]
        z_starts = [b[0] for b in zeros_blocks]
        z_ends = [b[1] for b in zeros_blocks]

        results = []
        for li, ri in queries:
            initial_ones = pref[ri+1] - pref[li]
            
            # Tradeable '1' blocks: must be fully in [li+1, ri-1] and surrounded by '0's
            idx_o_start = bisect_left(o_starts, li + 1)
            idx_o_end = bisect_right(o_ends, ri - 1) - 1
            min_o = query_min_o(idx_o_start, idx_o_end) if num_o > 0 else float('inf')
            
            # Tradeable '0' blocks: fully in [li, ri], surrounded by '1's in augmented
            idx_z_start = bisect_left(z_starts, li)
            idx_z_end = bisect_right(z_ends, ri) - 1
            max_z = query_max_z(idx_z_start, idx_z_end) if num_z > 0 else 0
            
            if min_o != float('inf') and max_z > 0:
                results.append(max(initial_ones, initial_ones - min_o + max_z))
            else:
                results.append(initial_ones)
        return results
# @lc code=end