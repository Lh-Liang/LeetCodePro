#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#
# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        s = list(s)
        answer = []
        
        for query in queries:
            if query[0] == 1:
                j = query[1]
                s[j] = 'B' if s[j] == 'A' else 'A'
            else:
                l, r = query[1], query[2]
                last = s[l]
                count = 1
                for i in range(l + 1, r + 1):
                    if s[i] != last:
                        count += 1
                        last = s[i]
                min_deletions = (r - l + 1) - count
                answer.append(min_deletions)
        
        return answer
# @lc code=end