#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        s_int = [int(c) for c in s]
        
        # Precompute prefix sums for all 5 characters
        prefix = [[0] * (n + 1) for _ in range(5)]
        for i in range(n):
            char_idx = s_int[i]
            for c in range(5):
                prefix[c][i+1] = prefix[c][i]
            prefix[char_idx][i+1] += 1
            
        ans = -float('inf')
        
        # Iterate over all pairs of distinct characters (a, b)
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                
                # min_val stores the minimum (prefix_a[i] - prefix_b[i]) 
                # for each parity combination (prefix_a % 2, prefix_b % 2)
                min_val = [[float('inf')] * 2 for _ in range(2)]
                last_b_pos = -1
                processed_i = -1
                
                # diff_prefix stores prefix_a[i] - prefix_b[i]
                # parity_a stores prefix_a[i] % 2
                # parity_b stores prefix_b[i] % 2
                
                for j in range(1, n + 1):
                    if s_int[j-1] == b:
                        last_b_pos = j - 1
                    
                    # Valid i must satisfy: i <= j - k AND substring s[i:j] contains 'b'
                    # Substring s[i:j] contains 'b' if i <= last_b_pos
                    limit = j - k
                    if last_b_pos < limit:
                        limit = last_b_pos
                    
                    # Update min_val for all newly available i up to limit
                    while processed_i < limit:
                        processed_i += 1
                        pa = prefix[a][processed_i] % 2
                        pb = prefix[b][processed_i] % 2
                        val = prefix[a][processed_i] - prefix[b][processed_i]
                        if val < min_val[pa][pb]:
                            min_val[pa][pb] = val
                    
                    # Current parities at index j
                    cur_pa = prefix[a][j] % 2
                    cur_pb = prefix[b][j] % 2
                    
                    # We need (prefix_a[j] - prefix_a[i]) to be odd -> parity_a[i] != cur_pa
                    # We need (prefix_b[j] - prefix_b[i]) to be even -> parity_b[i] == cur_pb
                    target_pa = 1 - cur_pa
                    target_pb = cur_pb
                    
                    if min_val[target_pa][target_pb] != float('inf'):
                        res = (prefix[a][j] - prefix[b][j]) - min_val[target_pa][target_pb]
                        if res > ans:
                            ans = res
                            
        return int(ans)
# @lc code=end