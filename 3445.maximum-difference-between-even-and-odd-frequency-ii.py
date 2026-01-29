#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = -float('inf')
        
        # Precompute prefix sums for each digit 0-4
        pref = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            val = int(s[i])
            for d in range(5):
                pref[d][i+1] = pref[d][i] + (1 if d == val else 0)
        
        # Iterate over all pairs of distinct digits (a, b)
        # a: odd frequency char, b: even frequency char
        for a in range(5):
            for b in range(5):
                if a == b: continue
                
                # Pre-calculate first occurrence of each prefix sum value for b
                # to handle the 'non-zero frequency' constraint efficiently.
                first_occ_b = {}
                for idx, val in enumerate(pref[b]):
                    if val not in first_occ_b: 
                        first_occ_b[val] = idx
                
                # min_lookup[parity_a][parity_b] stores min(pref[a][i] - pref[b][i])
                min_lookup = [[float('inf')] * 2 for _ in range(2)]
                ptr = 0
                
                for j in range(k, n + 1):
                    # Valid i must satisfy: 
                    # 1. i <= j - k (Length constraint)
                    # 2. pref[b][i] < pref[b][j] (Non-zero frequency constraint)
                    # Because pref[b] is non-decreasing, pref[b][i] < pref[b][j] 
                    # is equivalent to i < first_occ_b[pref[b][j]]
                    limit = min(j - k, first_occ_b[pref[b][j]] - 1)
                    
                    while ptr <= limit:
                        pa, pb = pref[a][ptr] % 2, pref[b][ptr] % 2
                        val = pref[a][ptr] - pref[b][ptr]
                        if val < min_lookup[pa][pb]:
                            min_lookup[pa][pb] = val
                        ptr += 1
                    
                    # To make freq[a] odd: pref[a][j] % 2 != pref[a][i] % 2
                    # To make freq[b] even: pref[b][j] % 2 == pref[b][i] % 2
                    target_pa = 1 - (pref[a][j] % 2)
                    target_pb = pref[b][j] % 2
                    
                    if min_lookup[target_pa][target_pb] != float('inf'):
                        diff = (pref[a][j] - pref[b][j]) - min_lookup[target_pa][target_pb]
                        if diff > ans:
                            ans = diff
                            
        return int(ans)
# @lc code=end