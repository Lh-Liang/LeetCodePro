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

        # Precompute prefix sums for costs to convert to each character 'a'-'z'
        costs = [[0] * (n + 1) for _ in range(26)]
        for c_idx in range(26):
            target_char_code = ord('a') + c_idx
            s = 0
            for i in range(n):
                s += abs(ord(caption[i]) - target_char_code)
                costs[c_idx][i + 1] = s

        def get_cost(c_idx, start, length):
            return costs[c_idx][start + length] - costs[c_idx][start]

        inf = float('inf')
        dp = [inf] * (n + 1)
        dp[n] = 0
        
        # best_trans[i] = (char_index, block_length)
        best_trans = [None] * (n + 1)
        # first_char[i] = char_index of the first block in optimal suffix i
        first_char = [None] * (n + 1)
        # diff_char[i] = char_index of the first character in optimal suffix i that != first_char[i]
        diff_char = [None] * (n + 1)

        for i in range(n - 3, -1, -1):
            for c in range(26):
                for k in (3, 4, 5):
                    if i + k > n:
                        break
                    
                    cost_ik = get_cost(c, i, k) + dp[i + k]
                    if cost_ik > dp[i]:
                        continue
                    
                    is_better = False
                    if cost_ik < dp[i]:
                        is_better = True
                    else:
                        # Tie-break: Lexicographical comparison of (c*k + Suffix[i+k])
                        old_c, old_k = best_trans[i]
                        if c < old_c:
                            is_better = True
                        elif c == old_c:
                            # Compare shorter vs longer block when character is same
                            k_min, k_max = (k, old_k) if k < old_k else (old_k, k)
                            # We essentially compare (c * (k_max-k_min) + Suffix[i+k_max]) 
                            # vs (Suffix[i+k_min]). Since Suffix[i+k_min] starts with c, 
                            # we look for the first char in Suffix[i+k_min] that is not c.
                            d_idx = diff_char[i + k_min]
                            # If d_idx is None, suffix is all 'c's; if d_idx < c, shorter is better.
                            if d_idx is not None:
                                if k == k_min:
                                    if d_idx < c: is_better = True
                                else:
                                    if c < d_idx: is_better = True

                    if is_better:
                        dp[i] = cost_ik
                        best_trans[i] = (c, k)
                        first_char[i] = c
                        # The first character in suffix i+k that is not c
                        if first_char[i + k] is not None and first_char[i + k] != c:
                            diff_char[i] = first_char[i + k]
                        else:
                            diff_char[i] = diff_char[i + k]

        if dp[0] == inf:
            return ""

        res = []
        curr = 0
        while curr < n:
            c_idx, k = best_trans[curr]
            res.append(chr(ord('a') + c_idx) * k)
            curr += k
        return "".join(res)
# @lc code=end