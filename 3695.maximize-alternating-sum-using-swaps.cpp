#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#
# @lc code=start
class Solution {
public:
    vector<int> parent;
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }
    
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        parent.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // Build union-find structure
        for (const auto& swap : swaps) {
            unite(swap[0], swap[1]);
        }
        
        // Group indices by their root
        unordered_map<int, vector<int>> components;
        for (int i = 0; i < n; i++) {
            components[find(i)].push_back(i);
        }
        
        // For each component, optimize assignment
        vector<int> result(n);
        for (auto& [root, indices] : components) {
            // Collect values
            vector<int> values;
            for (int idx : indices) {
                values.push_back(nums[idx]);
            }
            
            // Sort indices by coefficient (even = +1, odd = -1) in descending order
            sort(indices.begin(), indices.end(), [](int a, int b) {
                int coefA = (a % 2 == 0) ? 1 : -1;
                int coefB = (b % 2 == 0) ? 1 : -1;
                return coefA > coefB;
            });
            
            // Sort values in descending order
            sort(values.begin(), values.end(), greater<int>());
            
            // Assign values
            for (int i = 0; i < indices.size(); i++) {
                result[indices[i]] = values[i];
            }
        }
        
        // Calculate alternating sum
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                sum += result[i];
            } else {
                sum -= result[i];
            }
        }
        
        return sum;
    }
};
# @lc code=end