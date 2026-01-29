#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Precompute prefix arrays for 'AA' and 'BB'
        count_AA = [0] * n
        count_BB = [0] * n
        
        # Initialize prefix counts for existing string
        for i in range(1, n):
            count_AA[i] = count_AA[i-1]
            count_BB[i] = count_BB[i-1]
            if s[i] == s[i-1]:
                if s[i] == 'A':
                    count_AA[i] += 1
                else:
                    count_BB[i] += 1
        
        result = []
        s = list(s)  # Convert string to list for mutability
        
        for query in queries:
            if query[0] == 1:  # Flip operation
                j = query[1]
                # Flip character at index j
                original_char = s[j]
                new_char = 'A' if original_char == 'B' else 'B'
                s[j] = new_char
                
                # Adjust counts around index j after flip
                if j > 0:
                    if s[j-1] == original_char:
                        if original_char == 'A':
                            count_AA[j:] = [x-1 for x in count_AA[j:]]
                        else:
                            count_BB[j:] = [x-1 for x in count_BB[j:]]
                    elif s[j-1] == new_char:
                        if new_char == 'A':
                            count_AA[j:] = [x+1 for x in count_AA[j:]]
                        else:
                            count_BB[j:] = [x+1 for x in count_BB[j:]]
                if j < n-1:
                    if s[j+1] == original_char:
                        if original_char == 'A':
                            count_AA[j+2:] = [x-1 for x in count_AA[j+2:]]
                        else:
                            count_BB[j+2:] = [x-1 for x in count_BB[j+2:]]
                    elif s[j+1] == new_char:
                        if new_char == 'A':
                            count_AA[j+2:] = [x+1 for x in count_AA[j+2:]]
                        else:
                            count_BB[j+2:] = [x+1 for x in count_BB[j+2:]]
            elif query[0] == 2:  # Compute operation
                l, r = query[1], query[2]
                delete_AA = (count_AA[r] - (count_AA[l-1] if l > 0 else 0))
                delete_BB = (count_BB[r] - (count_BB[l-1] if l > 0 else 0))
                result.append(delete_AA + delete_BB)
        return result
# @lc code=end