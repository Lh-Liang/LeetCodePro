#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        word = []
        i = 0
        while i <= n - m:
            if str1[i] == 'T':
                word.extend(str2)
                i += m - 1 # skip next (m-1) indices as they're part of valid substring matching `str2`
            else:
                # Find smallest possible character not matching `str2` at this position
                # Add smallest lexicographic character that is not a part of `str2` substring starting from here.
                min_char = 'a' if 'a' != str2[0] else 'b' # Simplified assumption for mismatch case. Adjust logic if necessary.
                word.append(min_char)
            i += 1
        # If we reach end without fulfilling all conditions return empty string or complete remainder with smallest characters. 
        if len(word) < n + m - 1: 
            word.extend(['a'] * (m - (len(word) - n))) # Fill remaining with smallest chars if needed 
        return ''.join(word) if len(word) == n + m - 1 else '' 
# @lc code=end