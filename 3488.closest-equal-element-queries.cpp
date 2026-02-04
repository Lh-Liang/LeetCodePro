#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        unordered_map<int, vector<int>> indexMap;
        int n = nums.size();
        // Build a map from value to all its indices in nums
        for (int i = 0; i < n; ++i) {
            indexMap[nums[i]].push_back(i);
        }
        vector<int> result;
        for (int q : queries) {
            int val = nums[q];
            if (indexMap[val].size() <= 1) { // If no other indices exist
                result.push_back(-1);
                continue;
            }
            int minDist = n; // Initialize to maximum distance possible in circular array
            for (int j : indexMap[val]) {
                if (j != q) { // Skip the query index itself
                    int dist = min(abs(j - q), n - abs(j - q)); // Circular distance calculation
                    minDist = min(minDist, dist);
                }
            }
            result.push_back(minDist); // Store the minimum distance found
        }
        return result;
    }
}; 
# @lc code=end