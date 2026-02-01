#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#

# @lc code=start
#include <vector>
#include <bitset>
#include <numeric>

using namespace std;

class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        if (n == 0) return 0;

        // Convert each property list into a bitset of unique values (1-100)
        vector<bitset<101>> bitsets(n);
        for (int i = 0; i < n; ++i) {
            for (int val : properties[i]) {
                bitsets[i].set(val);
            }
        }

        // DSU setup
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        int components = n;

        auto find = [&](auto self, int i) -> int {
            return parent[i] == i ? i : parent[i] = self(self, parent[i]);
        };

        auto unite = [&](int i, int j) {
            int rootI = find(find, i);
            int rootJ = find(find, j);
            if (rootI != rootJ) {
                parent[rootI] = rootJ;
                components--;
                return true;
            }
            return false;
        };

        // Check all pairs for edges based on the intersection threshold k
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                // The number of distinct common integers is the count of set bits in the AND result
                if ((int)(bitsets[i] & bitsets[j]).count() >= k) {
                    unite(i, j);
                }
            }
        }

        return components;
    }
};
# @lc code=end