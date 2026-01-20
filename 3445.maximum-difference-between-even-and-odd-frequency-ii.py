```python
#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        # Map for digits '0'-'4'
        # Precompute prefix counts for each digit
        # prefix_counts[i][d] is the count of digit d in s[:i]
        prefix_counts = [[0] * 5 for _ in range(n + 1)]
        for i, char in enumerate(s):
            digit = int(char)
            for d in range(5):
                prefix_counts[i+1][d] = prefix_counts[i][d]
            prefix_counts[i+1][digit] += 1
            
        max_diff = -float('inf')
        
        # Iterate over all ordered pairs of distinct digits (odd_char, even_char)
        # We want to maximize: count(odd_char) - count(even_char)
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                
                # min_vals[parity_a][parity_b] stores the minimum (count(a) - count(b))
                # seen so far for a valid starting index i.
                # parity_a, parity_b are 0 or 1.
                min_vals = [[float('inf')] * 2 for _ in range(2)]
                
                current_valid_idx = 0
                last_pos_b = -1
                
                for j in range(1, n + 1):
                    # Update last position of character b
                    # s is 0-indexed, so s[j-1] is the character we just added to the prefix
                    if int(s[j-1]) == b:
                        last_pos_b = j - 1
                    
                    # We need to find an index i such that:
                    # 1. Length constraint: j - i >= k  =>  i <= j - k
                    # 2. Even char constraint: count(b) in s[i:j] > 0
                    #    This means index i must be <= last_pos_b
                    #    (i.e., the substring must start at or before the last occurrence of b)
                    
                    upper_bound_i = min(j - k, last_pos_b)
                    
                    # Update the min_vals with all newly valid indices i
                    while current_valid_idx <= upper_bound_i:
                        count_a = prefix_counts[current_valid_idx][a]
                        count_b = prefix_counts[current_valid_idx][b]
                        diff = count_a - count_b
                        p_a = count_a % 2
                        p_b = count_b % 2
                        
                        if diff < min_vals[p_a][p_b]:
                            min_vals[p_a][p_b] = diff
                        
                        current_valid_idx += 1
                    
                    # If we have a potentially valid window length
                    if j >= k:
                        curr_count_a = prefix_counts[j][a]
                        curr_count_b = prefix_counts[j][b]
                        curr_diff = curr_count_a - curr_count_b
                        curr_p_a = curr_count_a % 2
                        curr_p_b = curr_count_b % 2
                        
                        # We need substring count(a) to be odd:
                        # (curr_count_a - prev_count_a) % 2 == 1
                        # => prev_count_a has different parity from curr_count_a
                        target_p_a = 1 - curr_p_a
                        
                        # We need substring count(b) to be even:
                        # (curr_count_b - prev_count_b) % 2 == 0
                        # => prev_count_b has same parity as curr_count_b
                        target_p_b = curr_p_b
                        
                        if min_vals[target_p_a][target_p_b] != float('inf'):
                            current_best = curr_diff - min_vals[target_p_a][target_p_b]
                            if current_best > max_diff:
                                max_diff = current_best
                                
        return max_diff if max_diff != -float('inf') else -1
# @lc code=end
```