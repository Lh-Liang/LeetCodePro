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
        for (int i = 0; i < n; i++) {
            for (int x : properties[i]) {
                bs[i][x] = 1;
            }
        }
        vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        auto find = [&](int x) -> int {
            int root = x;
            while (parent[root] != root) {
                root = parent[root];
            }
            int cur = x;
            while (cur != root) {
                int nxt = parent[cur];
                parent[cur] = root;
                cur = nxt;
            }
            return root;
        };
        auto unite = [&](int a, int b) {
            int pa = find(a);
            int pb = find(b);
            if (pa != pb) {
                parent[pa] = pb;
            }
        };
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                size_t inter = (bs[i] & bs[j]).count();
                if (inter >= static_cast<size_t>(k)) {
                    unite(i, j);
                }
            }
        }
        int comp = 0;
        for (int i = 0; i < n; i++) {
            if (find(i) == i) comp++;
        }
        return comp;
    }
};
# @lc code=end