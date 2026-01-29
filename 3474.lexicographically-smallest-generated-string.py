#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        best = ["z" * (n + m - 1)] # Initialize with high lexicographical value
        
        def backtrack(index, current):
            if index == n + m - 1:
                # If we've constructed a complete valid word
                if current < best[0]:
                    best[0] = current
                return
            
            if index >= n:
                return
            
            if str1[index] == 'T':
                # Ensure we can place str2 starting at this index if it fits within current bounds
                if index + m <= len(current):
                    next_word = current[:index] + str2 + current[index+m:]
                    backtrack(index + m, next_word)
            else: # str1[index] == 'F'
                for char in "abcdefghijklmnopqrstuvwxyz":
                    # Try all characters but ensure it creates a mismatch with str2
                    mismatch_found = False
                    for i in range(m):
                        if char != str2[i]:
                            mismatch_found = True
                            next_word = current[:index] + char + current[index+1:]
                            backtrack(index + 1, next_word)
                            break # Stop after finding one mismatch option to explore further paths
                    if mismatch_found:
                        break
        
        initial_string = "z" * (m - 1) # Initialize with empty start of appropriate length with placeholders like 'z'
        backtrack(0, initial_string)
        return best[0] if best[0] != "z" * (m - 1) else ""
# @lc code=end