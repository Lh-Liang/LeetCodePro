# @lc app=leetcode id=3782 lang=cpp
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution {
public:
    long long lastInteger(long long n) {
        if (n == 1) return 1;
        return 2 * lastInteger(n / 2) - (n % 2 == 0 ? 1 : -1);
    }
};
# @lc code=end