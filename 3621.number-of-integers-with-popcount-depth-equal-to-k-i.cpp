# @lc app=leetcode id=3621 lang=cpp

# [3621] Number of Integers With Popcount-Depth Equal to K I

# @lc code=start
class Solution {
public:
    long long popcountDepth(long long n, int k) {
        auto popcount = [](long long x) {
            return __builtin_popcountll(x);
        };
        int count = 0;
        for (long long i = 1; i <= n; ++i) {
            int depth = 0;
            long long x = i;
            while (x != 1) {
                x = popcount(x);
                ++depth;
            }
            if (depth == k) {
                ++count;
            }
        }
        return count;
    }
};
# @lc code=end