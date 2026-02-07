#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#
# @lc code=start
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        unordered_map<int, vector<int>> index_map;
        int n = nums.size();
        // Fill hashmap with indices for each value in nums
        for (int i = 0; i < n; ++i) {
            index_map[nums[i]].push_back(i);
        }
        vector<int> result;
        // Process each query
        for (int query : queries) {
            int target = nums[query];
            if (index_map[target].size() == 1) { // Only one occurrence of target value
                result.push_back(-1);
                continue;
            }
            int min_distance = INT_MAX;
            // Find minimum distance in a circular manner
            for (int idx : index_map[target]) {
                if (idx != query) { // Don't compare with itself
                    int dist_cw = (idx - query + n) % n; // Clockwise distance
                    int dist_ccw = (query - idx + n) % n; // Counter-clockwise distance
                    min_distance = min(min_distance, min(dist_cw, dist_ccw));
                }
            }
            result.push_back(min_distance);
        } 
        return result; 
    } 
}; 
# @lc code=end