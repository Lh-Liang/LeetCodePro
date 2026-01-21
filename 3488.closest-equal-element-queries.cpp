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
        
        // Create a map from value to indices
        unordered_map<int, vector<int>> valueToIndices;
        for (int i = 0; i < n; i++) {
            valueToIndices[nums[i]].push_back(i);
        }
        
        vector<int> answer;
        for (int queryIdx : queries) {
            int value = nums[queryIdx];
            vector<int>& indices = valueToIndices[value];
            
            // If only one index with this value, return -1
            if (indices.size() == 1) {
                answer.push_back(-1);
                continue;
            }
            
            int minDist = INT_MAX;
            for (int j : indices) {
                if (j != queryIdx) {
                    int dist = min(abs(j - queryIdx), n - abs(j - queryIdx));
                    minDist = min(minDist, dist);
                }
            }
            
            answer.push_back(minDist);
        }
        
        return answer;
    }
};
# @lc code=end