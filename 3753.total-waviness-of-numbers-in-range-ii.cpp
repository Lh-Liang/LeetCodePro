#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution {
public:
    long long totalWaviness(long long num1, long long num2) {
        return getWaviness(num2) - getWaviness(num1 - 1);
    }
private:
    using ll = long long;
    // dp[pos][tight][prev1][prev2][lead_zero]
    ll dp[20][2][11][11][2];
    string S;
    int N;
    // Recursive DP function
    ll dfs(int pos, int tight, int prev1, int prev2, int lead_zero, int count) {
        if (pos == N) return count;
        if (dp[pos][tight][prev1][prev2][lead_zero] != -1) return dp[pos][tight][prev1][prev2][lead_zero];
        ll res = 0;
        int up = tight ? (S[pos] - '0') : 9;
        for (int d = 0; d <= up; ++d) {
            int nlead_zero = lead_zero && d == 0;
            int nprev1 = nlead_zero ? 10 : d;
            int nprev2 = prev1;
            int ntight = (tight && d == up);
            int ncount = count;
            // Only check for peak/valley if we have at least three digits (no leading zeros)
            if (!lead_zero && prev2 != 10 && prev1 != 10) {
                if (prev1 > prev2 && prev1 > d) ncount += 1;
                if (prev1 < prev2 && prev1 < d) ncount += 1;
            }
            res += dfs(pos + 1, ntight, nprev1, nprev2, nlead_zero, ncount);
        }
        return dp[pos][tight][prev1][prev2][lead_zero] = res;
    }
    ll getWaviness(ll num) {
        if (num < 100) return 0; // No waviness for numbers < 100
        S = to_string(num);
        N = S.size();
        memset(dp, -1, sizeof(dp));
        // prev1 and prev2 set to 10 to indicate 'no digit yet'
        return dfs(0, 1, 10, 10, 1, 0);
    }
};
# @lc code=end