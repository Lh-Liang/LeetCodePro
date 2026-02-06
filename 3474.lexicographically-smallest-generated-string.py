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
        result = [''] * (n + m - 1)
        i = 0
        while i <= n - m:
            if str1[i] == 'T':
                result[i:i+m] = list(str2)
            else:
                # Construct a non-matching segment by altering a character in str2 minimally.
                non_matching_segment = list(str2)
                # Try replacements using multiple alternatives to ensure non-match and minimal lexicographical impact.
                for j in range(m):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        if char != str2[j]:
                            non_matching_segment[j] = char
                            break
                    break  # Only change one character to ensure minimal change.
                result[i:i+m] = non_matching_segment
            i += 1
        # Fill remaining parts with smallest lexicographical values if needed.
        for j in range(n+m-1):
            if result[j] == '':
                result[j] = 'a'
        # Verify if constructed result meets all conditions of T and F before returning.
        for k in range(n):
            current_substring = ''.join(result[k:k+m])
            if (str1[k] == 'T' and current_substring != str2) or (str1[k] == 'F' and current_substring == str2):
                return ""
        return ''.join(result)
# @lc code=end