#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        // Map to store sorted indices for each number
        unordered_map<int, vector<int>> positions;
        for (int i = 0; i < n; ++i) {
            positions[nums[i]].push_back(i);
        }

        vector<int> result;
        result.reserve(queries.size());

        for (int q : queries) {
            int val = nums[q];
            const vector<int>& pos = positions[val];
            int k = pos.size();

            if (k <= 1) {
                result.push_back(-1);
                continue;
            }

            // Find the position of the current query index 'q' in the sorted list 'pos'
            // Since 'q' is guaranteed to be in 'pos', lower_bound will find it.
            auto it = lower_bound(pos.begin(), pos.end(), q);
            int idx_in_pos = distance(pos.begin(), it);

            // Identify the indices of the neighbors in the circular manner
            int left_neighbor_idx_in_pos = (idx_in_pos - 1 + k) % k;
            int right_neighbor_idx_in_pos = (idx_in_pos + 1) % k;

            int left_target_idx = pos[left_neighbor_idx_in_pos];
            int right_target_idx = pos[right_neighbor_idx_in_pos];

            // Helper lambda to calculate circular distance
            auto dist = [&](int i, int j) {
                int d = abs(i - j);
                return min(d, n - d);
            };

            int d1 = dist(q, left_target_idx);
            int d2 = dist(q, right_target_idx);

            result.push_back(min(d1, d2));
        }

        return result;
    }
};
# @lc code=end