#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#

# @lc code=start
#include <vector>
#include <bitset>
#include <numeric>
#include <set>

using namespace std;

class Solution {
public:
    struct DSU {
        vector<int> parent;
        int components;
        DSU(int n) : components(n) {
            parent.resize(n);
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        void unite(int i, int j) {
            int root_i = find(i);
            int root_j = find(j);
            if (root_i != root_j) {
                parent[root_i] = root_j;
                components--;
            }
        }
    };

    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        if (n == 0) return 0;

        // Convert each row to a bitset of unique values (values 1-100)
        vector<bitset<101>> bitsets(n);
        for (int i = 0; i < n; ++i) {
            for (int val : properties[i]) {
                bitsets[i].set(val);
            }
        }

        DSU dsu(n);

        // Compare every pair of nodes
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                // intersect(a, b) counts unique common integers
                // bitset intersection and count() gives exactly this
                if ((int)(bitsets[i] & bitsets[j]).count() >= k) {
                    dsu.unite(i, j);
                }
            }
        }

        return dsu.components;
    }
};
# @lc code=end