#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        
        if k == 0:
            return True
        
        # Precompute first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # Find all special substrings (as intervals [i, j])
        special_substrings = []
        
        for i in range(n):
            max_last = i
            
            for j in range(i, n):
                c = s[j]
                
                # If this character appeared before position i, break
                if first[c] < i:
                    break
                
                max_last = max(max_last, last[c])
                
                if max_last == j:
                    # Exclude the entire string
                    if not (i == 0 and j == n - 1):
                        special_substrings.append((i, j))
        
        # Find maximum number of disjoint intervals using greedy algorithm
        if not special_substrings:
            return False
        
        # Sort by ending position
        special_substrings.sort(key=lambda x: x[1])
        
        # Greedy selection
        count = 1
        last_end = special_substrings[0][1]
        
        for i in range(1, len(special_substrings)):
            if special_substrings[i][0] > last_end:
                count += 1
                last_end = special_substrings[i][1]
        
        return count >= k
# @lc code=end