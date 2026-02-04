#
# @lc app=leetcode id=3782 lang=cpp
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution {
public:
    long long lastInteger(long long n) {
        long long start = 1;
        long long step = 1;
        bool left = true;
        while (n > 1) {
            if (left || n % 2 == 1) { // if going left or odd count, update start
                start += step;
            }
            n /= 2; // halve the count of numbers remaining
            step *= 2; // double the step size for next round
            left = !left; // alternate direction
        }
        return start;
    }
};
# @lc code=end