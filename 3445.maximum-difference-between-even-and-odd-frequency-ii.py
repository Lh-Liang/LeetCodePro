#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        from collections import defaultdict, Counter
        n = len(s)
        max_diff = -1
        freq = Counter()
        odd_freq = defaultdict(int)
        even_freq = defaultdict(int)
        left = 0
        for right in range(n):
            # Add new character to frequency counter
            char_right = s[right]
            freq[char_right] += 1
            # Update odd/even status for this character
            if freq[char_right] % 2 == 0:
                even_freq[char_right] += 1
                if freq[char_right] > 1:
                    odd_freq[char_right] -= 1
            else:
                odd_freq[char_right] += 1
                if freq[char_right] > 1:
                    even_freq[char_right] -= 1
            
            # Check if window is valid (size at least k)
            while right - left + 1 >= k:
                # Calculate max difference between any odd and even frequency characters
                for a in odd_freq:
                    if odd_freq[a] > 0:
                        for b in even_freq:
                            if even_freq[b] > 0:
                                max_diff = max(max_diff, freq[a] - freq[b])
                # Shrink window from left
                char_left = s[left]
                if freq[char_left] % 2 == 0:
                    even_freq[char_left] -= 1
                else:
                    odd_freq[char_left] -= 1
                freq[char_left] -= 1
                left += 1
        return max_diff
# @lc code=end