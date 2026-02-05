#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution {
public:
    using ll = long long;
    ll dp[20][11][11][2][2];
    vector<int> digits;

    ll dfs(int pos, int prev1, int prev2, bool tight, bool start) {
        if (pos == digits.size()) return 0;
        if (dp[pos][prev1][prev2][tight][start] != -1) return dp[pos][prev1][prev2][tight][start];
        ll res = 0;
        int up = tight ? digits[pos] : 9;
        for (int d = 0; d <= up; ++d) {
            bool nstart = start || d > 0;
            bool ntight = tight && (d == up);
            if (!nstart) {
                res += dfs(pos + 1, 10, 10, ntight, nstart);
            } else {
                int wave = 0;
                if (prev2 != 10 && prev1 != 10) {
                    if (prev1 > prev2 && prev1 > d) ++wave;
                    if (prev1 < prev2 && prev1 < d) ++wave;
                }
                res += dfs(pos + 1, d, prev1, ntight, nstart) + wave + 0LL;
            }
        }
        return dp[pos][prev1][prev2][tight][start] = res;
    }

    ll waviness(ll x) {
        digits.clear();
        while (x) {
            digits.push_back(x % 10);
            x /= 10;
        }
        if (digits.empty()) digits.push_back(0);
        reverse(digits.begin(), digits.end());
        memset(dp, -1, sizeof(dp));
        return dfs(0, 10, 10, 1, 0);
    }

    long long totalWaviness(long long num1, long long num2) {
        return waviness(num2) - waviness(num1 - 1);
    }
};
# @lc code=end