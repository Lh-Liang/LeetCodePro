//
// @lc app=leetcode id=3743 lang=cpp
//
// [3743] Maximize Cyclic Partition Score
//

// @lc code=start
class Solution {
public:
    using ll = long long;
    int n;
    vector<vector<int>> min_st, max_st;
    vector<int> log2s;

    void buildSparseTable(const vector<int>& arr) {
        int N = arr.size();
        int max_log = 32 - __builtin_clz(N);
        min_st.assign(N, vector<int>(max_log));
        max_st.assign(N, vector<int>(max_log));
        log2s.assign(N + 1, 0);
        for (int i = 2; i <= N; ++i) log2s[i] = log2s[i / 2] + 1;
        for (int i = 0; i < N; ++i) {
            min_st[i][0] = arr[i];
            max_st[i][0] = arr[i];
        }
        for (int j = 1; (1 << j) <= N; ++j) {
            for (int i = 0; i + (1 << j) <= N; ++i) {
                min_st[i][j] = min(min_st[i][j-1], min_st[i+(1<<(j-1))][j-1]);
                max_st[i][j] = max(max_st[i][j-1], max_st[i+(1<<(j-1))][j-1]);
            }
        }
    }
    int query_min(int l, int r) { // [l, r]
        int len = r - l + 1;
        int j = log2s[len];
        return min(min_st[l][j], min_st[r-(1<<j)+1][j]);
    }
    int query_max(int l, int r) {
        int len = r - l + 1;
        int j = log2s[len];
        return max(max_st[l][j], max_st[r-(1<<j)+1][j]);
    }
    ll dp_solve(int start, int k, int rem_len, const vector<int>& arr, vector<vector<vector<ll>>>& dp) {
        if (k == 1) {
            int mi = query_min(start, start+rem_len-1);
            int ma = query_max(start, start+rem_len-1);
            return ma - mi;
        }
        if (dp[start][k][rem_len] != -1) return dp[start][k][rem_len];
        ll ans = 0;
        for (int len = 1; len <= rem_len - (k - 1); ++len) {
            int l = start, r = start + len - 1;
            int mi = query_min(l, r);
            int ma = query_max(l, r);
            ll score = ma - mi + dp_solve((r+1), k-1, rem_len-len, arr, dp);
            ans = max(ans, score);
        }
        return dp[start][k][rem_len] = ans;
    }
    long long maximumScore(vector<int>& nums, int k) {
        n = nums.size();
        vector<int> arr(nums);
        arr.insert(arr.end(), nums.begin(), nums.end()); // duplicate for cyclic
        buildSparseTable(arr);
        ll res = 0;
        for (int start = 0; start < n; ++start) {
            // Use a fresh DP table for each rotation to ensure state isolation
            vector<vector<vector<ll>>> dp(2*n+1, vector<vector<ll>>(k+2, vector<ll>(n+1, -1)));
            res = max(res, dp_solve(start, k, n, arr, dp));
        }
        return res;
    }
};
// @lc code=end