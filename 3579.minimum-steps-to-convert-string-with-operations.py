#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        
        def calculate_ops(s1, s2):
            # Calculate minimum operations to transform s1 to s2
            # using only swaps and replacements (no reverse)
            length = len(s1)
            mismatches = []
            for i in range(length):
                if s1[i] != s2[i]:
                    mismatches.append(i)
            
            if not mismatches:
                return 0
            
            ops = 0
            used = [False] * len(mismatches)
            
            # Greedily find swaps to fix pairs of mismatches
            for i in range(len(mismatches)):
                if used[i]:
                    continue
                pos_i = mismatches[i]
                for j in range(i + 1, len(mismatches)):
                    if used[j]:
                        continue
                    pos_j = mismatches[j]
                    # Check if swapping pos_i and pos_j fixes both
                    if s1[pos_i] == s2[pos_j] and s1[pos_j] == s2[pos_i]:
                        ops += 1
                        used[i] = True
                        used[j] = True
                        break
            
            # Remaining mismatches need replacements
            for i in range(len(mismatches)):
                if not used[i]:
                    ops += 1
            
            return ops
        
        def calculate_cost(i, j):
            # Cost to transform word1[i:j] to word2[i:j]
            s1 = word1[i:j]
            s2 = word2[i:j]
            
            # Option 1: without reverse
            cost1 = calculate_ops(s1, s2)
            
            # Option 2: with reverse (only if length > 1)
            if len(s1) > 1:
                cost2 = 1 + calculate_ops(s1[::-1], s2)
                return min(cost1, cost2)
            else:
                return cost1
        
        # Dynamic Programming
        # dp[i] = minimum operations to transform word1[0:i] to word2[0:i]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            # Try all possible last substrings ending at position i
            for j in range(i):
                cost = calculate_cost(j, i)
                dp[i] = min(dp[i], dp[j] + cost)
        
        return dp[n]
# @lc code=end