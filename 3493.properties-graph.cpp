#
# @lc app=leetcode id=3493 lang=cpp
#
# [3493] Properties Graph
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>

using namespace std;

class Solution {
public:
    // Standard DSU implementation
    struct DSU {
        vector<int> parent;
        int count;
        
        DSU(int n) : count(n) {
            parent.resize(n);
            iota(parent.begin(), parent.end(), 0);
        }
        
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        
        void unite(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent[rootX] = rootY;
                count--;
            }
        }
    };

    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        
        // Preprocess: sort and unique each property list to handle "distinct integers"
        // and make intersection checks efficient.
        for (int i = 0; i < n; ++i) {
            sort(properties[i].begin(), properties[i].end());
            properties[i].erase(unique(properties[i].begin(), properties[i].end()), properties[i].end());
        }
        
        DSU dsu(n);
        
        // Check every pair
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                // Calculate intersection size of two sorted unique vectors
                int common = 0;
                int idx1 = 0, idx2 = 0;
                int size1 = properties[i].size();
                int size2 = properties[j].size();
                
                while (idx1 < size1 && idx2 < size2) {
                    if (properties[i][idx1] < properties[j][idx2]) {
                        idx1++;
                    } else if (properties[i][idx1] > properties[j][idx2]) {
                        idx2++;
                    } else {
                        common++;
                        idx1++;
                        idx2++;
                    }
                }
                
                if (common >= k) {
                    dsu.unite(i, j);
                }
            }
        }
        
        return dsu.count;
    }
};
# @lc code=end