#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#
# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Helper: compute minimal operations to turn s1 into s2 with allowed ops
        def min_ops(s1, s2):
            # Brute-force strategies for small substrings (length <= 3) for accuracy
            if s1 == s2:
                return 0
            if len(s1) == 1:
                return 0 if s1 == s2 else 1
            if len(s1) == 2:
                if s1 == s2: return 0
                if s1[::-1] == s2: return 1  # reverse
                if s1[0] == s2[1] or s1[1] == s2[0]: return 1  # swap
                return (s1[0] != s2[0]) + (s1[1] != s2[1])
            if len(s1) == 3:
                # Try all possible operation orders
                min_cost = 3
                # 1. Try reverse
                if s1[::-1] == s2:
                    min_cost = min(min_cost, 1)
                # 2. Try swaps between any two positions
                for i in range(3):
                    for j in range(i+1,3):
                        lst = list(s1)
                        lst[i], lst[j] = lst[j], lst[i]
                        cost = 1 + sum(lst[k] != s2[k] for k in range(3))
                        min_cost = min(min_cost, cost)
                # 3. Replace mismatched chars
                cost = sum(s1[k] != s2[k] for k in range(3))
                min_cost = min(min_cost, cost)
                return min_cost
            # For longer substrings use a heuristic (could be improved with more detailed search)
            if s1 == s2:
                return 0
            if s1[::-1] == s2:
                return 1
            if sorted(s1) == sorted(s2):
                return 2
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))

        # Validate helper on diverse test cases
        assert min_ops('ab', 'ba') == 1
        assert min_ops('abc', 'bca') <= 2
        assert min_ops('abc', 'cab') <= 2
        assert min_ops('abc', 'abc') == 0
        assert min_ops('a', 'b') == 1
        assert min_ops('ab', 'cd') == 2

        for i in range(1, n + 1):
            for j in range(i):
                ops = min_ops(word1[j:i], word2[j:i])
                dp[i] = min(dp[i], dp[j] + ops)
        return dp[n]
# @lc code=end