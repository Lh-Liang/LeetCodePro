#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        s = list(s)
        res = []
        for q in queries:
            if q[0] == 1:
                # Flip character at index j
                j = q[1]
                s[j] = 'A' if s[j] == 'B' else 'B'
            else:
                # Compute minimum deletions for s[l..r]
                l, r = q[1], q[2]
                count = 0
                for i in range(l, r):
                    if s[i] == s[i+1]:
                        count += 1
                res.append(count)
        return res
# @lc code=end