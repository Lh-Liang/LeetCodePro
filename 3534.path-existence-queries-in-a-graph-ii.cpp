#
# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        if (n == 0) return {};

        // 1. Get unique sorted values
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        sorted_nums.erase(unique(sorted_nums.begin(), sorted_nums.end()), sorted_nums.end());
        int m = sorted_nums.size();

        // 2. Precompute jumps (Binary Lifting)
        // The maximum distance can be m-1. We need max_log such that 2^max_log >= m.
        int max_log = 0;
        while ((1 << max_log) < m) max_log++;
        if (max_log == 0) max_log = 1;
        
        vector<vector<int>> jump(m, vector<int>(max_log));

        for (int i = 0; i < m; ++i) {
            auto it = upper_bound(sorted_nums.begin(), sorted_nums.end(), sorted_nums[i] + maxDiff);
            jump[i][0] = distance(sorted_nums.begin(), prev(it));
        }

        for (int k = 1; k < max_log; ++k) {
            for (int i = 0; i < m; ++i) {
                jump[i][k] = jump[jump[i][k-1]][k-1];
            }
        }

        // 3. Process queries
        vector<int> results;
        results.reserve(queries.size());
        for (const auto& q : queries) {
            int u = q[0], v = q[1];
            if (u == v) {
                results.push_back(0);
                continue;
            }
            int val_u = nums[u], val_v = nums[v];
            if (val_u > val_v) swap(val_u, val_v);

            int idx_u = lower_bound(sorted_nums.begin(), sorted_nums.end(), val_u) - sorted_nums.begin();
            int idx_v = lower_bound(sorted_nums.begin(), sorted_nums.end(), val_v) - sorted_nums.begin();

            // Check reachability using the deepest level of the jump table
            // Since 2^(max_log-1) might be less than m-1, we use the property that
            // if we can't reach idx_v in the max power of 2 steps, we check if the
            // furthest possible node in the component reaches idx_v.
            int curr = idx_u;
            if (jump[curr][max_log - 1] < idx_v) {
                // Even with the largest jump, we might need more steps.
                // We can use the jump table to move as far as possible.
                for (int k = max_log - 1; k >= 0; --k) {
                    curr = jump[curr][k];
                }
                if (curr < idx_v) {
                    results.push_back(-1);
                    continue;
                }
            }

            // Binary lifting to find min steps
            int steps = 0;
            curr = idx_u;
            for (int k = max_log - 1; k >= 0; --k) {
                if (jump[curr][k] < idx_v) {
                    curr = jump[curr][k];
                    steps += (1 << k);
                }
            }
            results.push_back(steps + 1);
        }

        return results;
    }
};
# @lc code=end