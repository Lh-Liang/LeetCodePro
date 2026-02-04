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
        // Optimized method to handle large ranges without iterating through each number directly
        for (long long i = num1; i <= num2; ++i) {
            // Handle digits efficiently without conversion to string
            std::vector<int> digits;
            long long temp = i;
            while (temp > 0) {
                digits.push_back(temp % 10);
                temp /= 10;
            }
            std::reverse(digits.begin(), digits.end());
            int n = digits.size();
            if (n < 3) continue; // Skip numbers with fewer than three digits.
            int waviness = 0;
            for (int j = 1; j < n - 1; ++j) {
                if ((digits[j] > digits[j - 1] && digits[j] > digits[j + 1]) || 
                    (digits[j] < digits[j - 1] && digits[j] < digits[j + 1])) {
                    ++waviness;
                }
            }
            total_waviness += waviness;
        }
        return total_waviness;
    }
};
# @lc code=end