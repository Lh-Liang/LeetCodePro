
#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        # Since s consists only of digits '0' to '4', we have 5 possible characters
        # We'll use a prefix sum approach to count frequencies
        
        # For each character (0-4), we'll track prefix counts
        prefix_count = [[0]*5 for _ in range(n+1)]
        
        # Build prefix sum array
        for i in range(n):
            for c in range(5):
                prefix_count[i+1][c] = prefix_count[i][c]
            prefix_count[i+1][int(s[i])] += 1
        
        max_diff = float('-inf')
        
        # Check all substrings of length at least k
        for i in range(n - k + 1):
            for j in range(i + k - 1, n):
                # Get frequency of each character in substring s[i:j+1]
                freq = [0] * 5
                for c in range(5):
                    freq[c] = prefix_count[j+1][c] - prefix_count[i][c]
                
                # Find max odd frequency and max even (non-zero) frequency
                max_odd = -1
                max_even = -1
                
                for c in range(5):
                    if freq[c] > 0:
                        if freq[c] % 2 == 1:  # odd frequency
                            max_odd = max(max_odd, freq[c])
                        else:  # even frequency
                            max_even = max(max_even, freq[c])
                
                # If we have both odd and even frequencies
                if max_odd != -1 and max_even != -1:
                    max_diff = max(max_diff, max_odd - max_even)
        
        return max_diff if max_diff != float('-inf') else -1
# @lc code=end