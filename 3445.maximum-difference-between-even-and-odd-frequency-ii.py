#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        from collections import Counter
        n = len(s)
        max_diff = float('-inf')
        digits = ['0','1','2','3','4']
        # Sliding window for all window sizes [k, n]
        for window_size in range(k, n+1):
            freq = [0]*5
            # Fill initial window
            for i in range(window_size):
                freq[ord(s[i])-ord('0')] += 1
            # Check this window
            for a in range(5):
                if freq[a] % 2 == 1:
                    for b in range(5):
                        if b != a and freq[b] > 0 and freq[b] % 2 == 0:
                            max_diff = max(max_diff, freq[a] - freq[b])
            for start in range(1, n-window_size+1):
                # Slide window
                freq[ord(s[start-1])-ord('0')] -= 1
                freq[ord(s[start+window_size-1])-ord('0')] += 1
                for a in range(5):
                    if freq[a] % 2 == 1:
                        for b in range(5):
                            if b != a and freq[b] > 0 and freq[b] % 2 == 0:
                                max_diff = max(max_diff, freq[a] - freq[b])
        return max_diff if max_diff != float('-inf') else -1
# @lc code=end