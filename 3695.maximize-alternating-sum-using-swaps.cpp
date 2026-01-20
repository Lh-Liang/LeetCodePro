#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>

using namespace std;

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);

        // Standard DSU find with path compression
        function<int(int)> find = [&](int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        };

        // Process swaps to unify components
        for (const auto& s : swaps) {
            int root_u = find(s[0]);
            int root_v = find(s[1]);
            if (root_u != root_v) {
                parent[root_u] = root_v;
            }
        }

        // Group values and even-index counts by component
        vector<vector<int>> component_values(n);
        vector<int> even_counts(n, 0);

        for (int i = 0; i < n; ++i) {
            int root = find(i);
            component_values[root].push_back(nums[i]);
            if (i % 2 == 0) {
                even_counts[root]++;
            }
        }

        long long total_sum = 0;
        for (int i = 0; i < n; ++i) {
            // Skip empty components
            if (component_values[i].empty()) continue;

            // Sort values in descending order
            sort(component_values[i].begin(), component_values[i].end(), greater<int>());

            int evens = even_counts[i];
            // Assign largest values to even positions, smallest to odd positions
            for (int j = 0; j < (int)component_values[i].size(); ++j) {
                if (j < evens) {
                    total_sum += component_values[i][j];
                } else {
                    total_sum -= (long long)component_values[i][j];
                }
            }
        }

        return total_sum;
    }
};
# @lc code=end