#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#
# @lc code=start
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
        int px = find(x), py = find(y);
        if (px == py) return;
        if (rnk[px] < rnk[py]) swap(px, py);
        parent[py] = px;
        if (rnk[px] == rnk[py]) rnk[px]++;
    }
    
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        
        parent.resize(n);
        rnk.resize(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
        
        // Convert each property array to a set for distinct values
        vector<unordered_set<int>> sets(n);
        for (int i = 0; i < n; i++) {
            for (int val : properties[i]) {
                sets[i].insert(val);
            }
        }
        
        // Check pairs and union if intersection >= k
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Count intersection
                int count = 0;
                for (int val : sets[i]) {
                    if (sets[j].count(val)) {
                        count++;
                    }
                }
                if (count >= k) {
                    unite(i, j);
                }
            }
        }
        
        // Count connected components
        int components = 0;
        for (int i = 0; i < n; i++) {
            if (find(i) == i) components++;
        }
        
        return components;
    }
};
# @lc code=end