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
        unordered_map<int, vector<int>> valueToIndices;
        
        // Group indices by value
        for (int i = 0; i < n; i++) {
            valueToIndices[nums[i]].push_back(i);
        }
        
        // Precompute minimum distance for each index
        vector<int> minDist(n, -1);
        
        for (auto& p : valueToIndices) {
            vector<int>& indices = p.second;
            int m = indices.size();
            if (m == 1) continue; // Only one occurrence, distance is -1
            
            for (int i = 0; i < m; i++) {
                // Get left and right neighbors (with circular wraparound in the indices list)
                int left = (i - 1 + m) % m;
                int right = (i + 1) % m;
                
                // Calculate circular distances in the original array
                int d1 = abs(indices[i] - indices[left]);
                int d2 = abs(indices[i] - indices[right]);
                
                // Circular distance = min(direct, wraparound)
                int leftDist = min(d1, n - d1);
                int rightDist = min(d2, n - d2);
                
                minDist[indices[i]] = min(leftDist, rightDist);
            }
        }
        
        // Answer queries
        vector<int> result;
        for (int q : queries) {
            result.push_back(minDist[q]);
        }
        
        return result;
    }
};
# @lc code=end