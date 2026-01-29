#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        for num in range(num1, num2 + 1):
            str_num = str(num)
            waviness = 0
            # Check each middle digit to see if it's a peak or valley
            for i in range(1, len(str_num) - 1):
                if (str_num[i] > str_num[i - 1] and str_num[i] > str_num[i + 1]) or \
                   (str_num[i] < str_num[i - 1] and str_num[i] < str_num[i + 1]):
                    waviness += 1
            total_waviness += waviness
        return total_waviness
# @lc code=end