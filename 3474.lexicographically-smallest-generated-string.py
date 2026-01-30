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
        # Attempting to build the word lexicographically smallest
        for i in range(n):
            if str1[i] == 'T':
                # Append str2 since it must match here
                word.append(str2)
            else:
                # Append smallest possible character that does not form str2 starting at i
                # Choose characters that don't match str2 at this position
                if i + m <= n + m - 1:
                    if word[i:i+m] == list(str2):
                        # Adjust first character to break match with str2
                        alt_char = 'a' if str2[0] != 'a' else 'b'  # Choose a different start char than first of str2
                        word.append(alt_char + str2[1:])  # Replace first char of this segment with alternative char
                    else:
                        word.append(str2)  # If no conflict, append normally due to lack of other valid options.
        return ''.join(word[:(m+n-1)])  # Return constructed word or empty if not possible as per conditions. 
# @lc code=end