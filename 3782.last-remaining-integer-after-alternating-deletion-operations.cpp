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
        bool leftToRight = true;
        while (n > 1) {
            if (leftToRight || n % 2 == 1) {
                head += step;
            }
            n /= 2;
            step *= 2;
            leftToRight = !leftToRight;
        }
        return head;
    }
};
# @lc code=end