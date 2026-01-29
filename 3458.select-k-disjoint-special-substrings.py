#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
from typing import List
import math

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        if k == 0:
            return True
        a = ord('a')
        left_pos: List[int] = [-1] * 26
        right_pos: List[int] = [-1] * 26
        for i in range(n):
            idx = ord(s[i]) - a
            if left_pos[idx] == -1:
                left_pos[idx] = i
            right_pos[idx] = i
        left_arr: List[int] = [left_pos[ord(s[i]) - a] for i in range(n)]
        # Sparse table for RMQ min on left_arr
        logn = 0
        while (1 << logn) <= n:
            logn += 1
        st = [[0] * n for _ in range(logn)]
        for i in range(n):
            st[0][i] = left_arr[i]
        for j in range(1, logn):
            for i in range(n - (1 << j) + 1):
                st[j][i] = min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))])
        def get_min(ql: int, qr: int) -> int:
            if ql > qr:
                return n + 1
            length = qr - ql + 1
            k = 0
            while (1 << (k + 1)) <= length:
                k += 1
            return min(st[k][ql], st[k][qr - (1 << k) + 1])
        # Precompute obstruct[r]
        lastp: List[int] = [-1] * 26
        obstruct: List[int] = [-1] * n
        for r in range(n):
            idx = ord(s[r]) - a
            lastp[idx] = r
            maxo = -1
            for d in range(26):
                if right_pos[d] != -1 and right_pos[d] > r:
                    maxo = max(maxo, lastp[d])
            obstruct[r] = maxo
        # Greedy count
        cur_pos = 0
        cnt = 0
        while cur_pos < n and cnt < k:
            found_r = -1
            for r in range(cur_pos, n):
                lst = obstruct[r]
                lstart = 0 if lst == -1 else lst + 1
                lstart = max(lstart, cur_pos)
                if lstart > r:
                    continue
                good = False
                for d in range(26):
                    L = left_pos[d]
                    if L == -1 or L < lstart or L > r:
                        continue
                    mn = get_min(L + 1, r)
                    if mn >= L:
                        if not (L == 0 and r == n - 1):
                            good = True
                            break
                if good:
                    found_r = r
                    break
            if found_r == -1:
                break
            cnt += 1
            cur_pos = found_r + 1
        return cnt >= k

# @lc code=end