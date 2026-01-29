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
        
        inf = float('inf')
        dp = [inf] * (n + 1)
        best_char = [26] * (n + 1)
        
        dp[n] = 0
        ords = [ord(c) - ord('a') for c in caption]
        
        # DP to find min cost
        for i in range(n - 3, -1, -1):
            for c_idx in range(25, -1, -1):
                cost = 0
                for k in range(1, 6):
                    if i + k > n:
                        break
                    cost += abs(ords[i + k - 1] - c_idx)
                    if k >= 3:
                        res = cost + dp[i + k]
                        if res < dp[i]:
                            dp[i] = res
                            best_char[i] = c_idx
                        elif res == dp[i]:
                            best_char[i] = c_idx # Lexicographically smaller character is checked last
        
        if dp[0] == inf:
            return ""
            
        # Reconstruction
        res = []
        i = 0
        while i < n:
            char_idx = best_char[i]
            char = chr(ord('a') + char_idx)
            
            # Determine the best length k among 3, 4, 5
            best_k = -1
            for k in [3, 4, 5]:
                if i + k <= n:
                    cost_k = sum(abs(ords[j] - char_idx) for j in range(i, i + k))
                    if cost_k + dp[i + k] == dp[i]:
                        if best_k == -1:
                            best_k = k
                        else:
                            # Compare current best_k suffix vs this k suffix
                            # Both start with 'char' * best_k. 
                            # Next char of shorter one is best_char[i + best_k]
                            # We want to keep the one that leads to smaller string
                            next_c = best_char[i + best_k]
                            if next_c < char_idx:
                                # Shorter is better, stay with best_k
                                pass
                            else:
                                # Longer (k) is better or same
                                best_k = k
            
            res.append(char * best_k)
            i += best_k
            
        return "".join(res)
# @lc code=end