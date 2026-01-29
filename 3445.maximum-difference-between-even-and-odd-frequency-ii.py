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
        # Precompute prefix counts for each digit '0'-'4'
        counts = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            digit = s_ints[i]
            for d in range(5):
                counts[d][i+1] = counts[d][i]
            counts[digit][i+1] += 1
            
        max_diff = -float('inf')
        
        # Iterate over all pairs of distinct digits (a, b)
        # a will have odd frequency, b will have even non-zero frequency
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                
                # min_vals[pa][pb] stores the minimum (counts[a][i] - counts[b][i])
                # where pa = counts[a][i]%2 and pb = counts[b][i]%2
                min_vals = [[float('inf')] * 2 for _ in range(2)]
                
                processed_i = 0
                last_b_idx = -1
                
                for j in range(1, n + 1):
                    if s_ints[j-1] == b:
                        last_b_idx = j - 1
                    
                    # Constraints for i: 
                    # 1. j - i >= k  => i <= j - k
                    # 2. freq[b] > 0 => i <= last_b_idx
                    target_i_bound = min(j - k, last_b_idx)
                    
                    while processed_i <= target_i_bound:
                        pa_i = counts[a][processed_i] % 2
                        pb_i = counts[b][processed_i] % 2
                        val_i = counts[a][processed_i] - counts[b][processed_i]
                        if val_i < min_vals[pa_i][pb_i]:
                            min_vals[pa_i][pb_i] = val_i
                        processed_i += 1
                    
                    pa_j = counts[a][j] % 2
                    pb_j = counts[b][j] % 2
                    val_j = counts[a][j] - counts[b][j]
                    
                    # Need (counts[a][j]-counts[a][i]) odd and (counts[b][j]-counts[b][i]) even
                    target_pa_i = 1 - pa_j
                    target_pb_i = pb_j
                    
                    if min_vals[target_pa_i][target_pb_i] != float('inf'):
                        diff = val_j - min_vals[target_pa_i][target_pb_i]
                        if diff > max_diff:
                            max_diff = diff
                            
        return int(max_diff)
# @lc code=end