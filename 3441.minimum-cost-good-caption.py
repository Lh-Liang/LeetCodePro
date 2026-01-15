#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

from typing import List

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        # Impossible because shortest good caption needs at least 3 characters.
        if n < 3:
            return ""
        
        # Convert characters to numbers 0..25
        x = [ord(ch) - ord('a') for ch in caption]
        
        # Prefix sums of x
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + x[i]
        
        # Gc[t]: count positions < t where x[pos] <= c
        # Hc[t]: sum   positions < t where x[pos] <= c
        Gc = [[0] * (n + 1) for _ in range(26)]
        Hc = [[0] * (n + 1) for _ in range(26)]
        
        for i in range(n):
            xi = x[i]
            for c in range(26):
                inc_g = int(xi <= c)
                inc_h = xi if xi <= c else 0
                Gc[c][i + 1] = Gc[c][i] + inc_g
                Hc[c][i + 1] = Hc[c][i] + inc_h
        
        # U(c,k) as defined
        U = [[0] * (n + 1) for _ in range(26)]
        for c in range(26):
            for k in range(n + 1):
                U[c][k] = c * (2 * Gc[c][k] - k) + pref_sum[k] - 2 * Hc[c][k]
        
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        best_prev = [-1] * (n + 1)
        best_char = [-1] * (n + 1)
        
        # For each character maintain the minimum value of dp[j] - U(c,j)
        min_vals = [(INF, -1)] * 26   # (value, argmin_index)
        
        # Initialize with j = 0
        for c in range(26):
            val = dp[0] - U[c][0]
            min_vals[c] = (val, 0)
        
        # Main DP loop
        for i in range(1, n + 1):
            # Consider transitions ending at i (prefix length i)
            # Segment must have length at least 3 -> start index j <= i - 3
            if i >= 3:
                for c in range(26):
                    val_min, argmin_j = min_vals[c]
                    cand_cost = U[c][i] + val_min
                    if cand_cost < dp[i]:
                        dp[i] = cand_cost
                        best_prev[i] = argmin_j
                        best_char[i] = c
            
            # Update min_vals using current state i
            if dp[i] != INF:
                for c in range(26):
                    val_update = dp[i] - U[c][i]
                    if val_update < min_vals[c][0]:
                        min_vals[c] = (val_update, i)
        
        # Impossible
        if dp[n] == INF:
            return ""
        
        # Reconstruct answer
        parts = []
        idx = n
        while idx > 0:
            prev_idx = best_prev[idx]
            ch_num = best_char[idx]
            seg_len = idx - prev_idx
            parts.append(chr(ch_num + ord('a')) * seg_len)
            idx = prev_idx
        parts.reverse()
        return "".join(parts)
# @lc code=end