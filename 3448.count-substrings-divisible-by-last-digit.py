#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for j in range(n):
            d = int(s[j])
            if d == 0:
                continue
            
            num_mod = 0
            power = 1
            for i in range(j, -1, -1):
                num_mod = (int(s[i]) * power + num_mod) % d
                if num_mod == 0:
                    count += 1
                power = (power * 10) % d
        
        return count
# @lc code=end