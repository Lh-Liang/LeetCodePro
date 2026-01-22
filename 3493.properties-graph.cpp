//
// @lc app=leetcode id=3493 lang=cpp
//
// [3493] Properties Graph
//

// @lc code=start
class Solution {
private:
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
    
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        
        // Convert each properties[i] to a set for distinct values
        vector<set<int>> sets(n);
        for (int i = 0; i < n; i++) {
            for (int val : properties[i]) {
                sets[i].insert(val);
            }
        }
        
        // Union-Find initialization
        parent.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // Check all pairs
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
            if (find(i) == i) {
                components++;
            }
        }
        
        return components;
    }
};
// @lc code=end