#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3493 lang=cpp
 *
 * [3493] Properties Graph
 */

// @lc code=start
class Solution {
    struct DSU {
        vector<int> p, r;
        DSU(int n) : p(n), r(n, 0) {
            iota(p.begin(), p.end(), 0);
        }
        int find(int x) {
            if (p[x] == x) return x;
            return p[x] = find(p[x]);
        }
        void unite(int a, int b) {
            a = find(a); b = find(b);
            if (a == b) return;
            if (r[a] < r[b]) swap(a, b);
            p[b] = a;
            if (r[a] == r[b]) r[a]++;
        }
    };

public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = (int)properties.size();
        vector<bitset<101>> mask(n);

        for (int i = 0; i < n; i++) {
            for (int v : properties[i]) {
                if (1 <= v && v <= 100) mask[i].set(v);
            }
        }

        DSU dsu(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (((mask[i] & mask[j]).count()) >= (size_t)k) {
                    dsu.unite(i, j);
                }
            }
        }

        int components = 0;
        for (int i = 0; i < n; i++) {
            if (dsu.find(i) == i) components++;
        }
        return components;
    }
};
// @lc code=end
