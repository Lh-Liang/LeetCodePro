#
# @lc app=leetcode id=3704 lang=cpp
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution {
public:
    long long countNoZeroPairs(long long n) {
        auto isNoZero = [](long long x) {
            while (x > 0) {
                if (x % 10 == 0) return false;
                x /= 10;
            }
            return true;
        };
        long long count = 0;
        for (long long a = 1; a < n; ++a) {
            long long b = n - a;
            if (isNoZero(a) && isNoZero(b)) {
                ++count;
            }
        }
        return count;
    }
};
# @lc code=end