#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution {
public:
    long long totalWaviness(long long num1, long long num2) {
        long long total_waviness = 0;
        for (long long num = num1; num <= num2; ++num) {
            std::string s = std::to_string(num);
            int n = s.length();
            if (n < 3) continue; // Skip numbers with less than 3 digits
            for (int i = 1; i < n - 1; ++i) {
                if ((s[i] > s[i-1] && s[i] > s[i+1]) || (s[i] < s[i-1] && s[i] < s[i+1])) {
                    ++total_waviness;
                }
            }
        }
        return total_waviness;
    }
};
# @lc code=end