#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#
# @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        constexpr int MOD = 1e9+7;
        int m = mat.size();
        unordered_map<int, int> dp;
        // Initialize dp with the first row
        for (int v : mat[0]) dp[v]++;
        // Process each subsequent row
        for (int i = 1; i < m; ++i) {
            unordered_map<int, int> next;
            for (auto& [g, count] : dp) {
                for (int v : mat[i]) {
                    int ng = gcd(g, v);
                    next[ng] = (next[ng] + count) % MOD;
                }
            }
            dp = std::move(next);
        }
        return dp.count(1) ? dp[1] : 0;
    }
    int gcd(int a, int b) {
        while (b) { int t = b; b = a % b; a = t; }
        return a;
    }
};
# @lc code=end