#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""

        # Precompute prefix costs for each character a-z
        # cost_pref[c][i] is the cost to change caption[0...i-1] to char c
        cost_pref = [[0] * (n + 1) for _ in range(26)]
        for c in range(26):
            target_val = ord('a') + c
            for i in range(n):
                cost_pref[c][i+1] = cost_pref[c][i] + abs(ord(caption[i]) - target_val)

        def get_cost(i, L, c_idx):
            return cost_pref[c_idx][i + L] - cost_pref[c_idx][i]

        # dp[i] = (min_cost, best_char_idx, best_length)
        inf = float('inf')
        dp = [(inf, 26, 0)] * (n + 1)
        dp[n] = (0, 26, 0) # Base case: end of string

        for i in range(n - 3, -1, -1):
            best_cost = inf
            best_c = 26
            best_L = 0

            for c in range(26):
                # Check possible lengths that could start a new block
                for L in (3, 4, 5):
                    if i + L > n:
                        break
                    
                    res_cost, next_c, _ = dp[i + L]
                    if res_cost == inf:
                        continue
                    
                    current_total = get_cost(i, L, c) + res_cost
                    
                    # Comparison logic for lexicographical smallest string
                    is_better = False
                    if current_total < best_cost:
                        is_better = True
                    elif current_total == best_cost:
                        if c < best_c:
                            is_better = True
                        elif c == best_c:
                            # Tie-break lengths: Compare current char c with the 
                            # first char of the suffix starting at the divergence point.
                            # The divergence point between (c, L_old) and (c, L_new) 
                            # is i + min(L_old, L_new).
                            L_small, L_large = (L, best_L) if L < best_L else (best_L, L)
                            # At index i + L_small, the 'large' path has char 'c'
                            # The 'small' path has char dp[i + L_small].best_c
                            char_in_small_path = dp[i + L_small][1]
                            
                            # If L is the larger one and c < char_in_small_path, L is better
                            # If L is the smaller one and c < char_in_small_path, L_old was better
                            if L > best_L:
                                if c < char_in_small_path: is_better = True
                            else:
                                if c > char_in_small_path: is_better = True

                    if is_better:
                        best_cost, best_c, best_L = current_total, c, L
            
            dp[i] = (best_cost, best_c, best_L)

        if dp[0][0] == inf:
            return ""

        # Reconstruct string
        res = []
        curr = 0
        while curr < n:
            _, c_idx, L = dp[curr]
            res.append(chr(ord('a') + c_idx) * L)
            curr += L
        return "".join(res)
# @lc code=end