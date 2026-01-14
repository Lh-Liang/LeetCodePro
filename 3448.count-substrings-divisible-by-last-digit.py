#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        # For divisibility by 3 and 6
        count3 = [0, 0, 0]
        count3[0] = 1
        prefix_sum_mod3 = 0
        
        # For divisibility by 9
        count9 = [0] * 9
        count9[0] = 1
        prefix_sum_mod9 = 0
        
        # For divisibility by 7
        count7 = [0] * 7
        count7[0] = 1
        prefix_mod7 = 0
        pow10_inv_mod7 = 1  # 10^(-1) ≡ 5 (mod 7)
        
        for j in range(n):
            d = int(s[j])
            
            # Update prefix values for position j+1
            prefix_sum_mod3_new = (prefix_sum_mod3 + d) % 3
            prefix_sum_mod9_new = (prefix_sum_mod9 + d) % 9
            prefix_mod7_new = (prefix_mod7 * 10 + d) % 7
            pow10_inv_mod7 = (pow10_inv_mod7 * 5) % 7
            adjusted_new = (prefix_mod7_new * pow10_inv_mod7) % 7
            
            if d == 0:
                pass
            elif d == 1 or d == 2 or d == 5:
                result += j + 1
            elif d == 3:
                result += count3[prefix_sum_mod3_new]
            elif d == 4:
                result += 1  # single digit "4"
                if j >= 1:
                    last_two = int(s[j-1]) * 10 + 4
                    if last_two % 4 == 0:
                        result += j
            elif d == 6:
                result += count3[prefix_sum_mod3_new]
            elif d == 7:
                result += count7[adjusted_new]
            elif d == 8:
                result += 1  # single digit "8"
                if j >= 1:
                    last_two = int(s[j-1]) * 10 + 8
                    if last_two % 8 == 0:
                        result += 1
                if j >= 2:
                    last_three = int(s[j-2]) * 100 + int(s[j-1]) * 10 + 8
                    if last_three % 8 == 0:
                        result += j - 1
            elif d == 9:
                result += count9[prefix_sum_mod9_new]
            
            # Update counts
            count3[prefix_sum_mod3_new] += 1
            count9[prefix_sum_mod9_new] += 1
            count7[adjusted_new] += 1
            
            prefix_sum_mod3 = prefix_sum_mod3_new
            prefix_sum_mod9 = prefix_sum_mod9_new
            prefix_mod7 = prefix_mod7_new
        
        return result
# @lc code=end