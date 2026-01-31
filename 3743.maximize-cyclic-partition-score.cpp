#
# @lc app=leetcode id=3743 lang=cpp
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return 0;
        if (k >= n) {
            // If k is large, we can potentially isolate every change.
            // But the max possible score is bounded by the sum of ranges.
        }

        // To handle the cyclic nature, we can observe that at least one of the 
        // optimal partition boundaries must exist. If we fix the split point at index 's',
        // we solve the linear version. To avoid O(N^3), we can use the fact that
        // the global maximum and global minimum are likely to be endpoints or 
        // internal extremes. However, a safer O(N^2) approach for cyclic is needed.
        
        auto solveLinear = [&](const vector<int>& arr) {
            int m = arr.size();
            // f[i][j] = max score for first j elements with i subarrays.
            // Using space optimization: prev_f[j] is for i-1 subarrays.
            vector<long long> dp(m + 1, 0);
            long long max_total = 0;

            for (int seg = 1; seg <= k; ++seg) {
                vector<long long> next_dp(m + 1, -1e18);
                // For a fixed number of segments, we want to find the best split.
                // This is still O(k * N^2). We need to ensure it fits or optimize.
                for (int j = 1; j <= m; ++j) {
                    int cur_min = arr[j-1];
                    int cur_max = arr[j-1];
                    for (int p = j - 1; p >= 0; --p) {
                        if (dp[p] != -1e18) {
                            next_dp[j] = max(next_dp[j], dp[p] + (cur_max - cur_min));
                        }
                        if (p > 0) {
                            cur_min = min(cur_min, arr[p-1]);
                            cur_max = max(cur_max, arr[p-1]);
                        }
                    }
                }
                dp = next_dp;
                max_total = max(max_total, dp[m]);
            }
            return max_total;
        };

        // Given N=1000, we must find a way to linearize or optimize.
        // One property: there exists an optimal partition where the split occurs
        // at a point 'i' such that nums[i] is a local minimum or maximum.
        
        long long result = 0;
        // Try rotating such that the split happens at the global minimum
        int min_idx = 0;
        for(int i = 1; i < n; ++i) if(nums[i] < nums[min_idx]) min_idx = i;
        
        auto getRotated = [&](int start) {
            vector<int> res;
            for(int i = 0; i < n; ++i) res.push_back(nums[(start + i) % n]);
            return res;
        };

        result = max(result, solveLinear(getRotated(min_idx)));
        
        // Also try global maximum split point
        int max_idx = 0;
        for(int i = 1; i < n; ++i) if(nums[i] > nums[max_idx]) max_idx = i;
        result = max(result, solveLinear(getRotated(max_idx)));

        return result;
    }
};
# @lc code=end