#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
            
        n = len(word1)
        
        def get_min_ops_for_segment(s: str, t: str) -> int:
            def calculate_cost(char_s, char_t):
                diff_indices = []
                for i in range(len(char_s)):
                    if char_s[i] != char_t[i]:
                        diff_indices.append(i)
                
                if not diff_indices:
                    return 0
                
                # Count occurrences of specific character mismatches (a -> b)
                mismatch_counts = {}
                for idx in diff_indices:
                    pair = (char_s[idx], char_t[idx])
                    mismatch_counts[pair] = mismatch_counts.get(pair, 0) + 1
                
                # A swap saves 1 operation if we find a (a->b) and (b->a) pair
                saved_by_swaps = 0
                seen_pairs = set()
                for (a, b), count in mismatch_counts.items():
                    if (a, b) in seen_pairs: 
                        continue
                    if (b, a) in mismatch_counts:
                        saved_by_swaps += min(count, mismatch_counts[(b, a)])
                        seen_pairs.add((a, b))
                        seen_pairs.add((b, a))
                
                return len(diff_indices) - saved_by_swaps

            # Case 1: No reverse
            cost_no_rev = calculate_cost(s, t)
            # Case 2: Using a reverse (costs 1 op)
            cost_with_rev = 1 + calculate_cost(s[::-1], t)
            
            return min(cost_no_rev, cost_with_rev)

        # Precompute segment costs to optimize DP
        segment_costs = [[0] * (n + 1) for _ in range(n + 1)]
        for start in range(n):
            for end in range(start + 1, n + 1):
                segment_costs[start][end] = get_min_ops_for_segment(word1[start:end], word2[start:end])

        # dp[i] is min operations for prefix of length i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] + segment_costs[j][i] < dp[i]:
                    dp[i] = dp[j] + segment_costs[j][i]
        
        return int(dp[n])
# @lc code=end