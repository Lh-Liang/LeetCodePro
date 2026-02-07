# @lc app=leetcode id=3594 lang=cpp
# [3594] Minimum Time to Transport All Individuals
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <limits>
#include <unordered_map>
using namespace std;

class Solution {
public:
    double minTime(int n, int k, int m, vector<int>& time, vector<double>& mul) {
        unordered_map<int, double> memo; // Memoization map for storing states
        
        function<double(int,int,int)> dfs = [&](int mask, int stage, int remaining) -> double {
            if (remaining == 0) return 0; // All crossed over
            if (memo.count(mask)) return memo[mask];
            
            double min_time = numeric_limits<double>::max();
            
            // Try all combinations of up to k individuals using a bitmask approach
            for (int i = 0; i < (1 << n); ++i) { // Loop over all subsets of people
                if (__builtin_popcount(i) > k || (mask & i) != i) continue; // Skip invalid sets
                
                double max_cross_time = 0;
                for (int j = 0; j < n; ++j) {
                    if (i & (1 << j)) {
                        max_cross_time = max(max_cross_time, time[j] * mul[stage]);
                    }
                }
                int new_stage = (stage + static_cast<int>(floor(max_cross_time))) % m;
                double sub_result = dfs(mask ^ i, new_stage, remaining - __builtin_popcount(i));
                if (sub_result >= 0) {
                    min_time = min(min_time, max_cross_time + sub_result);
                }
            }
            
            return memo[mask] = (min_time == numeric_limits<double>::max()) ? -1 : min_time;
        };
        
        return dfs((1 << n) - 1, 0, n);
    }
};
# @lc code=end