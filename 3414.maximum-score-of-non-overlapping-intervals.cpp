// @lc app=leetcode id=3414 lang=cpp
//
// [3414] Maximum Score of Non-overlapping Intervals
//

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<pair<pair<int,int>, pair<int,int>>> arr; // ((end, start), (weight, orig_idx))
        for (int i = 0; i < n; ++i) {
            arr.push_back({{intervals[i][1], intervals[i][0]}, {intervals[i][2], i}});
        }
        sort(arr.begin(), arr.end());
        // Precompute previous non-overlapping interval for each interval
        vector<int> prev(n, -1);
        for (int i = 0; i < n; ++i) {
            int l = 0, r = i-1, ans = -1;
            while (l <= r) {
                int m = (l + r) / 2;
                if (arr[m].first.first < arr[i].first.second) { // arr[m].end < arr[i].start
                    ans = m;
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            prev[i] = ans;
        }
        // dp[i][k]: max weight for first i+1 intervals with k intervals chosen
        // Also track the corresponding indices for lex smallest
        vector<vector<long long>> dp(n, vector<long long>(5, 0));
        vector<vector<vector<int>>> idxs(n, vector<vector<int>>(5));
        for (int i = 0; i < n; ++i) {
            for (int k = 1; k <= 4; ++k) {
                // Option 1: don't take this interval
                if (i > 0) {
                    dp[i][k] = dp[i-1][k];
                    idxs[i][k] = idxs[i-1][k];
                }
                // Option 2: take this interval
                long long cand = arr[i].second.first;
                vector<int> cand_idxs = {arr[i].second.second};
                if (prev[i] != -1 && k > 1) {
                    cand += dp[prev[i]][k-1];
                    cand_idxs = idxs[prev[i]][k-1];
                    cand_idxs.push_back(arr[i].second.second);
                }
                // Lexicographical order is maintained through DP construction
                if (cand > dp[i][k] || (cand == dp[i][k] && (idxs[i][k].empty() || lexicographical_compare(cand_idxs.begin(), cand_idxs.end(), idxs[i][k].begin(), idxs[i][k].end())))) {
                    dp[i][k] = cand;
                    idxs[i][k] = cand_idxs;
                }
            }
        }
        // Find the best among k = 1..4
        long long best = 0;
        vector<int> answer;
        for (int k = 1; k <= 4; ++k) {
            if (dp[n-1][k] > best || (dp[n-1][k] == best && (answer.empty() || lexicographical_compare(idxs[n-1][k].begin(), idxs[n-1][k].end(), answer.begin(), answer.end())))) {
                best = dp[n-1][k];
                answer = idxs[n-1][k];
            }
        }
        // General verification step: check non-overlap and size constraints
        for (int i = 1; i < (int)answer.size(); ++i) {
            int idx_prev = answer[i-1];
            int idx_cur = answer[i];
            if (!(intervals[idx_prev][1] < intervals[idx_cur][0])) {
                // Overlapping found, should not happen
                return {};
            }
        }
        if (answer.size() > 4) return {};
        return answer;
    }
};
// @lc code=end