#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        result = []
        s = list(s)  # Convert string to list for mutability
        
        def flip(index):
            s[index] = 'B' if s[index] == 'A' else 'A'
            
        def calculate_min_deletions(l, r):
            deletions1 = deletions2 = 0
            expected1 = 'A'  # Start pattern 'ABAB...'
            expected2 = 'B'  # Start pattern 'BABA...'
            for i in range(l, r + 1):
                if s[i] != expected1:
                    deletions1 += 1
                if s[i] != expected2:
                    deletions2 += 1
                expected1 = 'B' if expected1 == 'A' else 'A'
                expected2 = 'B' if expected2 == 'A' else 'A'
            return min(deletions1, deletions2)
        
        for query in queries:
            if query[0] == 1:
                flip(query[1])
            elif query[0] == 2:
                result.append(calculate_min_deletions(query[1], query[2]))
        return result
# @lc code=end