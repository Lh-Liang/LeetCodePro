#
# @lc app=leetcode id=3753 lang=java
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution {
    public long totalWaviness(long num1, long num2) {
        long totalWaviness = 0;
        for (long i = num1; i <= num2; i++) {
            String s = Long.toString(i);
            int waviness = 0;
            if (s.length() > 2) {
                for (int j = 1; j < s.length() - 1; j++) {
                    int prev = s.charAt(j - 1) - '0';
                    int current = s.charAt(j) - '0';
                    int next = s.charAt(j + 1) - '0';
                    if ((current > prev && current > next) || (current < prev && current < next)) {
                        waviness++;
                    }
                }
            }
            totalWaviness += waviness;
        }
        return totalWaviness;
    }
}
# @lc code=end