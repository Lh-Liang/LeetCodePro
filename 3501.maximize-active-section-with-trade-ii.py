#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        if n == 0: return [0] * len(queries)
        
        blocks = []
        curr_char = s[0]
        start = 0
        for i in range(1, n):
            if s[i] != curr_char:
                blocks.append((curr_char, start, i - 1))
                curr_char = s[i]
                start = i
        blocks.append((curr_char, start, n - 1))
        
        m = len(blocks)
        idx_to_block = [0] * n
        for i, (_, b_start, b_end) in enumerate(blocks):
            for j in range(b_start, b_end + 1):
                idx_to_block[j] = i

        total_ones = s.count('1')
        z_indices = [i for i, b in enumerate(blocks) if b[0] == '0']
        z_lens = [blocks[i][2] - blocks[i][1] + 1 for i in z_indices]
        
        def build_st(arr):
            if not arr: return []
            k = len(arr).bit_length()
            st = [[0] * len(arr) for _ in range(k)]
            st[0] = arr[:]
            for j in range(1, k):
                for i in range(len(arr) - (1 << j) + 1):
                    st[j][i] = max(st[j-1][i], st[j-1][i + (1 << (j-1))])
            return st

        def query_st(st, L, R):
            if L > R: return -float('inf')
            j = (R - L + 1).bit_length() - 1
            return max(st[j][L], st[j][R - (1 << j) + 1])

        st_z = build_st(z_lens)

        tradable_ones_idx = []
        gains_merge = []
        neg_len_one = []
        for i in range(m):
            if blocks[i][0] == '1' and i > 0 and i < m - 1 and blocks[i-1][0] == '0' and blocks[i+1][0] == '0':
                tradable_ones_idx.append(i)
                gains_merge.append((blocks[i-1][2]-blocks[i-1][1]+1) + (blocks[i+1][2]-blocks[i+1][1]+1))
                neg_len_one.append(-(blocks[i][2]-blocks[i][1]+1))
        
        st_merge = build_st(gains_merge)
        st_neg_len = build_st(neg_len_one)
        
        results = []
        for li, ri in queries:
            b_li, b_ri = idx_to_block[li], idx_to_block[ri]
            
            z_start_idx = bisect.bisect_left(z_indices, b_li)
            z_end_idx = bisect.bisect_right(z_indices, b_ri) - 1
            max_z = 0
            if z_start_idx <= z_end_idx:
                if z_start_idx + 1 <= z_end_idx - 1:
                    max_z = query_st(st_z, z_start_idx + 1, z_end_idx - 1)
                b_idx_first = z_indices[z_start_idx]
                max_z = max(max_z, blocks[b_idx_first][2] - max(li, blocks[b_idx_first][1]) + 1)
                b_idx_last = z_indices[z_end_idx]
                max_z = max(max_z, min(ri, blocks[b_idx_last][2]) - blocks[b_idx_last][1] + 1)

            t_start = bisect.bisect_left(tradable_ones_idx, b_li + 1)
            t_end = bisect.bisect_right(tradable_ones_idx, b_ri - 1) - 1
            
            best_gain = 0
            if t_start <= t_end:
                for t_idx in {t_start, t_end}:
                    i = tradable_ones_idx[t_idx]
                    len_z_prev = blocks[i-1][2] - max(li, blocks[i-1][1]) + 1
                    len_z_next = min(ri, blocks[i+1][2]) - blocks[i+1][1] + 1
                    len_one = blocks[i][2] - blocks[i][1] + 1
                    best_gain = max(best_gain, len_z_prev + len_z_next, max_z - len_one)
                
                if t_start + 1 <= t_end - 1:
                    best_gain = max(best_gain, query_st(st_merge, t_start + 1, t_end - 1))
                    best_gain = max(best_gain, max_z + query_st(st_neg_len, t_start + 1, t_end - 1))
            
            results.append(total_ones + best_gain)
        return results
# @lc code=end