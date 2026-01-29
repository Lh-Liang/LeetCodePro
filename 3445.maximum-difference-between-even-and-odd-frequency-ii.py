#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        s_ints = [int(c) for c in s]
        # Precompute prefix counts for all 5 characters
        P = [[0] * (n + 1) for _ in range(5)]
        for idx, char_val in enumerate(s_ints):
            for c in range(5):
                P[c][idx + 1] = P[c][idx] + (1 if char_val == c else 0)
        
        ans = -float('inf')
        INF = 10**9
        
        # Iterate through all pairs (a, b)
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                
                # Pre-fetch prefix sum lists to avoid repeated lookups
                Pa = P[a]
                Pb = P[b]
                
                # min_val[pa][pb] stores min (P_a[i] - P_b[i]) for eligible i
                # min_safe[pa][pb] stores min (P_a[i] - P_b[i]) where freq[b] > 0
                min_val = [[INF] * 2 for _ in range(2)]
                min_safe = [[INF] * 2 for _ in range(2)]
                
                last_b_idx = -1
                
                for j in range(n):
                    # Update last_b_idx and move unsafe mins to safe if 'b' is encountered
                    if s_ints[j] == b:
                        last_b_idx = j
                        for r in range(2):
                            v0, v1 = min_val[r][0], min_val[r][1]
                            if v0 < min_safe[r][0]: min_safe[r][0] = v0
                            if v1 < min_safe[r][1]: min_safe[r][1] = v1
                            min_val[r][0] = min_val[r][1] = INF
                    
                    # Check new eligible start index i
                    i = j - k + 1
                    if i >= 0:
                        pa_i, pb_i = Pa[i] % 2, Pb[i] % 2
                        val = Pa[i] - Pb[i]
                        
                        if i <= last_b_idx:
                            if val < min_safe[pa_i][pb_i]:
                                min_safe[pa_i][pb_i] = val
                        else:
                            if val < min_val[pa_i][pb_i]:
                                min_val[pa_i][pb_i] = val
                    
                    # Current state at j+1
                    cur_pa, cur_pb = Pa[j+1] % 2, Pb[j+1] % 2
                    cur_D = Pa[j+1] - Pb[j+1]
                    
                    # Requirement: (cur_pa - i_pa) % 2 == 1 (odd) and (cur_pb - i_pb) % 2 == 0 (even)
                    target_pa = 1 - cur_pa
                    target_pb = cur_pb
                    
                    cand = cur_D - min_safe[target_pa][target_pb]
                    if cand > ans:
                        ans = cand
                            
        return int(ans)
# @lc code=end