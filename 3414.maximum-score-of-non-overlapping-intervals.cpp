# @lc app=leetcode id=3414 lang=cpp
# [3414] Maximum Score of Non-overlapping Intervals

# @lc code=start
#include <vector>
#include <algorithm>
#include <set>
#include <tuple>

class Solution {
public:
    std::vector<int> maximumWeight(std::vector<std::vector<int>>& intervals) {
        // Sort intervals based on their end time (ri)
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });
        
        int n = intervals.size();
        std::vector<int> dp(n, 0);
        std::vector<std::set<int>> indices(n);
        dp[0] = intervals[0][2];
        indices[0].insert(0);

        for (int i = 1; i < n; ++i) {
            int l = intervals[i][0], w = intervals[i][2];
            dp[i] = w;
            indices[i].insert(i);
            
            // Binary search for non-overlapping interval using lambda function for custom comparator
            int low = 0, high = i - 1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (intervals[mid][1] < l) {
                    if (dp[mid] + w > dp[i]) {
                        dp[i] = dp[mid] + w;
                        indices[i] = indices[mid];
                        indices[i].insert(i);
                    }
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            
            // If not taking current interval gives a better result
            if (dp[i - 1] > dp[i]) {
                dp[i] = dp[i - 1];
                indices[i] = indices[i - 1];
            }		}		// Find lexicographically smallest set of at most four indices with max score		int maxScoreIndex = std::max_element(dp.begin(), dp.end()) - dp.begin(); auto resultIndices = indices[maxScoreIndex]; std::vector<int> result(resultIndices.begin(), resultIndices.end()); while (result.size() > 4) { result.pop_back(); } std::sort(result.begin(), result.end()); return result; } }; # @lc code=end