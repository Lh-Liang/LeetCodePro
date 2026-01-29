#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        lengths = []
        cur = n
        while cur >= 1:
            lengths.append(cur)
            if cur == 1:
                break
            cur = (cur + 1) // 2
        pos = 1
        for i in range(len(lengths) - 2, -1, -1):
            prev_len = lengths[i]
            j = i
            if j % 2 == 0:
                # left operation
                pos = 2 * pos - 1
            else:
                # right operation
                if prev_len % 2 == 0:
                    pos = 2 * pos
                else:
                    pos = 2 * pos - 1
        return pos
# @lc code=end