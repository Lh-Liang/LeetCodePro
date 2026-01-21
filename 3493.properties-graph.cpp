#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#
# @lc code=start
class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        
        // Union-Find data structure
        vector<int> parent(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        function<int(int)> find = [&](int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        };
        
        auto unite = [&](int x, int y) {
            int px = find(x);
            int py = find(y);
            if (px != py) {
                parent[px] = py;
            }
        };
        
        // Function to count intersection
        auto intersect = [](const vector<int>& a, const vector<int>& b) {
            set<int> setA(a.begin(), a.end());
            set<int> setB(b.begin(), b.end());
            int count = 0;
            for (int x : setA) {
                if (setB.count(x)) {
                    count++;
                }
            }
            return count;
        };
        
        // Build graph - check all pairs
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (intersect(properties[i], properties[j]) >= k) {
                    unite(i, j);
                }
            }
        }
        
        // Count connected components
        set<int> components;
        for (int i = 0; i < n; i++) {
            components.insert(find(i));
        }
        
        return components.size();
    }
};
# @lc code=end