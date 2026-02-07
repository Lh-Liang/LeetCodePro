#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution {
public:
    long long totalWaviness(long long num1, long long num2) {
        long long totalWaviness = 0;
        for (long long i = num1; i <= num2; ++i) {
            std::string s = std::to_string(i);
            int waviness = 0;
            if (s.length() > 2) { // Only consider numbers with at least 3 digits.
                for (int j = 1; j < s.length() - 1; ++j) {
                    if ((s[j] > s[j-1] && s[j] > s[j+1]) || (s[j] < s[j-1] && s[j] < s[j+1])) {
                        ++waviness; // Increment if it is a peak or valley.
                    }
                }
            }
            totalWaviness += waviness;
        }
        return totalWaviness;
    }
}; 
# @lc code=end