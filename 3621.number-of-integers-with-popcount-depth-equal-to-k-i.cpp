#
# @lc app=leetcode id=3621 lang=cpp
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
#include <unordered_map>
#include <vector>
#include <bitset>
class Solution {
public:
    long long dp(int x, int k, std::unordered_map<int, std::unordered_map<int, long long>>& memo) {
        if (k < 0) return 0;
        if (x == 1) return k == 0 ? 1 : 0;
        if (memo.count(x) && memo[x].count(k)) return memo[x][k];
        int next_x = __builtin_popcount(x);
        long long result = dp(next_x, k - 1, memo);
        memo[x][k] = result;
        return result;
    }
    long long popcountDepth(long long n, int k) {
        std::unordered_map<int, std::unordered_map<int, long long>> memo;
        long long count = 0;
        for (long long x = 1; x <= n; ++x) {
            count += dp(x, k, memo);
        }
        return count;
    }
};
# @lc code=end