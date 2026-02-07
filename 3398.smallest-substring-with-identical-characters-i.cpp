#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#
# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.length();
        int max_len = n;  // Initialize max_len with maximum possible length
        for (int char_type : {0, 1}) { // Try both '0' and '1' as base types for flipping
            int left = 0, right = 0, flips = 0;
            while (right < n) {
                // Increment flip count if current char is not matching char_type
                if (s[right] - '0' != char_type) {
                    flips++;
                }
                // If flips exceed numOps, move left pointer to reduce flip count
                while (flips > numOps) {
                    if (s[left] - '0' != char_type) {
                        flips--;
                    }
                    left++;
                }
                // Update minimal longest identical substring length found so far
                max_len = std::min(max_len, right - left + 1);
                right++; // Move right pointer forward
            }
        }
        return max_len; // Return smallest possible longest identical substring after operations.
    }
};
# @lc code=end