#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        
        def get_base_cost(s1: str, s2: str) -> int:
            mismatches = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    mismatches.append(i)
            
            r = len(mismatches)
            if r == 0:
                return 0
            
            # Count pairs (x, y) where s1[i]=x, s2[i]=y
            counts = {}
            for i in mismatches:
                pair = (s1[i], s2[i])
                counts[pair] = counts.get(pair, 0) + 1
            
            pairs_saved = 0
            seen = set()
            for (x, y), count in counts.items():
                if (x, y) in seen:
                    continue
                if (y, x) in counts:
                    if x == y:
                        # Should not happen in mismatches list
                        continue
                    num_pairs = min(count, counts[(y, x)])
                    pairs_saved += num_pairs
                    seen.add((x, y))
                    seen.add((y, x))
            
            # Each swap saves 1 operation compared to 2 replaces
            return r - pairs_saved

        # Precompute costs for all possible substrings [i:j]
        substring_costs = [[0] * (n + 1) for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub1 = word1[i:j]
                sub2 = word2[i:j]
                cost_no_rev = get_base_cost(sub1, sub2)
                cost_with_rev = 1 + get_base_cost(sub1[::-1], sub2)
                substring_costs[i][j] = min(cost_no_rev, cost_with_rev)

        # dp[i] = min operations for word1[0:i]
        dp = [0] + [float('inf')] * n
        for j in range(1, n + 1):
            for i in range(j):
                if dp[i] != float('inf'):
                    dp[j] = min(dp[j], dp[i] + substring_costs[i][j])
        
        return int(dp[n])
# @lc code=end