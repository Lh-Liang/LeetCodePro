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
        vector<bitset<101>> bs(n);
        for (int i = 0; i < n; ++i) {
            for (int num : properties[i]) {
                bs[i].set(num);
            }
        }
        
        vector<int> parent(n);
        vector<int> rank(n, 0);
        for (int i = 0; i < n; ++i) parent[i] = i;
        
        function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        
        auto unite = [&](int x, int y) {
            int rx = find(x);
            int ry = find(y);
            if (rx == ry) return;
            if (rank[rx] < rank[ry]) {
                parent[rx] = ry;
            } else if (rank[rx] > rank[ry]) {
                parent[ry] = rx;
            } else {
                parent[ry] = rx;
                rank[rx]++;
            }
        };
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int common = (bs[i] & bs[j]).count();
                if (common >= k) {
                    unite(i, j);
                }
            }
        }
        
        int components = 0;
        for (int i = 0; i < n; ++i) {
            if (find(i) == i) components++;

}

return components;
    }
};
# @lc code=end