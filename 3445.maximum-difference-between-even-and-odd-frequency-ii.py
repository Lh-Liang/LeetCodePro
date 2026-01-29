#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        digits = [int(c) for c in s]
        # Precompute prefix counts for digits 0-4
        pref = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            for d in range(5):
                pref[d][i + 1] = pref[d][i]
            pref[digits[i]][i + 1] += 1
            
        ans = -n
        
        # Iterate through all pairs of distinct digits (a, b)
        for a in range(5):
            for b in range(5):
                if a == b: continue
                
                # min_val[parity_a][parity_b] stores min(pref[a][i] - pref[b][i])
                min_val = [[float('inf')] * 2 for _ in range(2)]
                
                # p tracks the prefix index i such that j - i >= k
                # last_b_idx tracks the index of the most recent 'b' to ensure freq[b] > 0
                p = 0
                last_b_idx = -1
                
                for j in range(1, n + 1):
                    if digits[j-1] == b:
                        last_b_idx = j - 1
                    
                    # Valid start indices i must satisfy: i <= j - k AND i <= last_b_idx
                    # This ensures length >= k and at least one 'b' is in s[i:j]
                    limit = min(j - k, last_b_idx)
                    while p <= limit:
                        pa, pb = pref[a][p] % 2, pref[b][p] % 2
                        val = pref[a][p] - pref[b][p]
                        if val < min_val[pa][pb]:
                            min_val[pa][pb] = val
                        p += 1
                    
                    # Target parities for prefix i to make s[i:j] have freq[a] odd and freq[b] even
                    # (pref[a][j] - pref[a][i]) % 2 == 1  => pref[a][i] % 2 == 1 - pref[a][j] % 2
                    # (pref[b][j] - pref[b][i]) % 2 == 0  => pref[b][i] % 2 == pref[b][j] % 2
                    target_pa = 1 - (pref[a][j] % 2)
                    target_pb = pref[b][j] % 2
                    
                    if min_val[target_pa][target_pb] != float('inf'):
                        ans = max(ans, (pref[a][j] - pref[b][j]) - min_val[target_pa][target_pb])
                            
        return int(ans)
# @lc code=end