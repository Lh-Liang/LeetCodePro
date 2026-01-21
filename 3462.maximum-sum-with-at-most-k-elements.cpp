#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3462 lang=cpp
 *
 * [3462] Maximum Sum With at Most K Elements
 */

// @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        if (k == 0) return 0LL;

        int n = (int)grid.size();
        vector<int> candidates;
        candidates.reserve((size_t)min<long long>((long long)n * (long long)grid[0].size(),
                                                 accumulate(limits.begin(), limits.end(), 0LL)));

        for (int i = 0; i < n; i++) {
            int take = min<int>(limits[i], (int)grid[i].size());
            if (take <= 0) continue;

            auto row = grid[i];
            sort(row.begin(), row.end(), greater<int>());
            for (int j = 0; j < take; j++) candidates.push_back(row[j]);
        }

        if (candidates.empty()) return 0LL;

        int kk = min<int>(k, (int)candidates.size());
        if (kk == (int)candidates.size()) {
            long long ans = 0;
            for (int x : candidates) ans += x;
            return ans;
        }

        nth_element(candidates.begin(), candidates.begin() + kk, candidates.end(), greater<int>());
        long long ans = 0;
        for (int i = 0; i < kk; i++) ans += candidates[i];
        return ans;
    }
};
// @lc code=end
