//
// @lc app=leetcode id=3695 lang=cpp
//
// [3695] Maximize Alternating Sum Using Swaps
//
// @lc code=start
class Solution {
public:
    vector<int> parent, rnk;
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px == py) return;
        if (rnk[px] < rnk[py]) std::swap(px, py);
        parent[py] = px;
        if (rnk[px] == rnk[py]) rnk[px]++;
    }
    
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        parent.resize(n);
        rnk.resize(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
        
        for (auto& s : swaps) {
            unite(s[0], s[1]);
        }
        
        unordered_map<int, vector<int>> components;
        for (int i = 0; i < n; i++) {
            components[find(i)].push_back(i);
        }
        
        long long result = 0;
        
        for (auto& [root, indices] : components) {
            vector<long long> values;
            int evenCount = 0;
            for (int idx : indices) {
                values.push_back(nums[idx]);
                if (idx % 2 == 0) evenCount++;
            }
            
            sort(values.begin(), values.end(), greater<long long>());
            
            for (int i = 0; i < (int)values.size(); i++) {
                if (i < evenCount) {
                    result += values[i];
                } else {
                    result -= values[i];
                }
            }
        }
        
        return result;
    }
};
// @lc code=end