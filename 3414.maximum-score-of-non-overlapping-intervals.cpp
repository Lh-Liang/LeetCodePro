#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#
# @lc code=start
class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        
        // Create indexed intervals and sort by end time
        vector<array<int, 4>> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = {intervals[i][1], intervals[i][0], intervals[i][2], i};
        }
        sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[3] < b[3];
        });
        
        // dp[i][k] = {weight, indices}
        vector<vector<pair<long long, vector<int>>>> dp(n + 1, vector<pair<long long, vector<int>>>(5, {-1, {}}));
        dp[0][0] = {0, {}};
        
        for (int i = 1; i <= n; i++) {
            int end = arr[i-1][0];
            int start = arr[i-1][1];
            int weight = arr[i-1][2];
            int idx = arr[i-1][3];
            
            // Don't take interval i-1
            for (int k = 0; k <= 4; k++) {
                if (dp[i-1][k].first >= 0) {
                    if (dp[i][k].first < 0 || 
                        dp[i-1][k].first > dp[i][k].first ||
                        (dp[i-1][k].first == dp[i][k].first && dp[i-1][k].second < dp[i][k].second)) {
                        dp[i][k] = dp[i-1][k];
                    }
                }
            }
            
            // Take interval i-1: binary search
            int j = 0;
            if (i > 1) {
                int left = 0, right = i - 2;
                while (left <= right) {
                    int mid = left + (right - left) / 2;
                    if (arr[mid][0] < start) {
                        j = mid + 1;
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                }
            }
            
            for (int k = 0; k < 4; k++) {
                if (dp[j][k].first >= 0) {
                    long long new_weight = dp[j][k].first + weight;
                    vector<int> new_indices = dp[j][k].second;
                    new_indices.push_back(idx);
                    sort(new_indices.begin(), new_indices.end());
                    
                    if (dp[i][k+1].first < 0 ||
                        new_weight > dp[i][k+1].first ||
                        (new_weight == dp[i][k+1].first && new_indices < dp[i][k+1].second)) {
                        dp[i][k+1] = {new_weight, new_indices};
                    }
                }
            }
        }
        
        // Find best result
        long long max_weight = -1;
        vector<int> result;
        for (int k = 0; k <= 4; k++) {
            if (dp[n][k].first >= 0 && 
                (max_weight < 0 || 
                 dp[n][k].first > max_weight ||
                 (dp[n][k].first == max_weight && dp[n][k].second < result))) {
                max_weight = dp[n][k].first;
                result = dp[n][k].second;
            }
        }
        
        return result;
    }
};
# @lc code=end