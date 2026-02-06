#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        return self.josephus(n)
    
    def josephus(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            return (self.josephus(n - 1) + 2) % n or n
# @lc code=end