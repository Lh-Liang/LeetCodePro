#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        result = []
        s = list(s)  # To allow mutation of the string
        
        def min_deletions_to_alternate(l, r):
            # Calculate minimum deletions to make s[l:r+1] alternating
            del_count_1 = del_count_2 = 0
            for i in range(l, r + 1):
                expected_char_1 = 'A' if (i - l) % 2 == 0 else 'B'
                expected_char_2 = 'B' if (i - l) % 2 == 0 else 'A'
                if s[i] != expected_char_1:
                    del_count_1 += 1
                if s[i] != expected_char_2:
                    del_count_2 += 1
            return min(del_count_1, del_count_2)
        
        for query in queries:
            if query[0] == 1:
                _, j = query
                # Flip character at index j
                s[j] = 'B' if s[j] == 'A' else 'A'
            elif query[0] == 2:
                _, l, r = query
                # Calculate minimum deletions for substring s[l:r+1]
                result.append(min_deletions_to_alternate(l, r))
        return result
# @lc code=end