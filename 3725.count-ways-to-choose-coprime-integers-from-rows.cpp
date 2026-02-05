#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
#include <vector>
#include <numeric>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        const int MOD = 1e9 + 7, MAXVAL = 150;
        int m = mat.size();
        unordered_map<int, int> dp;
        // Initialize DP for the first row
        for (int v : mat[0]) {
            dp[v] = (dp[v] + 1) % MOD;
        }
        // Update DP for each subsequent row
        for (int i = 1; i < m; ++i) {
            unordered_map<int, int> new_dp;
            for (auto& [g, cnt] : dp) {
                for (int v : mat[i]) {
                    int ng = gcd(g, v);
                    new_dp[ng] = (new_dp[ng] + cnt) % MOD;
                }
            }
            dp = move(new_dp);
        }
        return dp.count(1) ? dp[1] : 0;
    }
};
# @lc code=end