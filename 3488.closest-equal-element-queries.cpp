#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        unordered_map<int, vector<int>> num_indices;
        int n = nums.size();
        // Step 1: Map each number to its indices.
        for (int i = 0; i < n; ++i) {
            num_indices[nums[i]].push_back(i);
        }
        vector<int> answer(queries.size(), -1);
        // Step 2: Calculate minimum distance for each query.
        for (int q = 0; q < queries.size(); ++q) {
            int query_idx = queries[q];
            int num = nums[query_idx];
            if (num_indices[num].size() <= 1) continue; // No other index with same value.
            int min_dist = INT_MAX;
            // Find minimum distance using circular calculation.
            for (int idx : num_indices[num]) {
                if (idx != query_idx) {
                    int dist = abs(idx - query_idx);
                    min_dist = min(min_dist, min(dist, n - dist)); // Circular distance calculation.
                }
            }
            answer[q] = min_dist;
        } 
        return answer; 
    } 
}; 
# @lc code=end