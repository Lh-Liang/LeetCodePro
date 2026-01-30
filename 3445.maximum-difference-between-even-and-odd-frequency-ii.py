#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        max_diff = float('-inf')
        for i in range(n):
            freq = [0] * 10  # Since digits are 0-9
            for j in range(i, n):
                freq[int(s[j])] += 1
                if j - i + 1 >= k:
                    odd_freq = [(f, idx) for idx, f in enumerate(freq) if f % 2 == 1]
                    even_freq = [(f, idx) for idx, f in enumerate(freq) if f > 0 and f % 2 == 0]
                    if odd_freq and even_freq:
                        max_a = max(odd_freq)[0]
                        min_b = min(even_freq)[0]
                        max_diff = max(max_diff, max_a - min_b)
        return max_diff if max_diff != float('-inf') else -1
# @lc code=end