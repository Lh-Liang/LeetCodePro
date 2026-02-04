#
# @lc app=leetcode id=3782 lang=cpp
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution {
public:
    long long lastInteger(long long n) {
        long long head = 1;
        long long step = 1;
        bool left = true;

        while (n > 1) {
            if (left || n % 2 == 1) {
                head += step;
            }
            n /= 2;
            step *= 2;
            left = !left;
        }
        return head;
    }
};
# @lc code=end