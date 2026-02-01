#
# @lc app=leetcode id=3414 lang=cpp
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

struct Interval {
    int l, r, w, id;
};

struct Result {
    long long score;
    vector<int> ids;
    
    Result() : score(0) {}

    bool operator>(const Result& other) const {
        if (score != other.score) return score > other.score;
        if (ids.empty()) return false;
        if (other.ids.empty()) return true;
        return ids < other.ids;
    }
};

class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals_in) {
        int n = intervals_in.size();
        vector<Interval> intervals(n);
        for (int i = 0; i < n; ++i) {
            intervals[i] = {intervals_in[i][0], intervals_in[i][1], intervals_in[i][2], i};
        }
        
        // Sort to process intervals by start time
        sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
            if (a.l != b.l) return a.l < b.l;
            if (a.r != b.r) return a.r < b.r;
            return a.id < b.id;
        });
        
        vector<int> starts(n);
        for (int i = 0; i < n; ++i) starts[i] = intervals[i].l;
        
        // dp[i][k] = max weight using suffix [i...n-1] with at most k intervals
        vector<vector<Result>> dp(n + 1, vector<Result>(5));
        
        for (int i = n - 1; i >= 0; --i) {
            // Find next interval that starts after current interval ends
            int next_idx = lower_bound(starts.begin() + i + 1, starts.end(), intervals[i].r + 1) - starts.begin();
            
            for (int k = 1; k <= 4; ++k) {
                // Choice 1: Don't take current interval
                dp[i][k] = dp[i + 1][k];
                
                // Choice 2: Take current interval
                Result take;
                take.score = (long long)intervals[i].w + dp[next_idx][k - 1].score;
                
                // Construct sorted indices for the 'take' option
                take.ids = dp[next_idx][k - 1].ids;
                take.ids.push_back(intervals[i].id);
                sort(take.ids.begin(), take.ids.end());
                
                if (take > dp[i][k]) {
                    dp[i][k] = take;
                }
            }
        }
        
        return dp[0][4].ids;
    }
};
# @lc code=end