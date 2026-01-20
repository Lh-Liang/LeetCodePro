#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#

# @lc code=start
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
    struct Edge {
        long long w;
        int u;
        int v;
        bool operator<(const Edge& other) const {
            return w < other.w;
        }
    };

    struct DSU {
        vector<int> parent;
        // relation[i] stores the parity of the path length from i to parent[i]
        // 0: same color, 1: different color
        vector<int> relation;

        DSU(int n) {
            parent.resize(n);
            iota(parent.begin(), parent.end(), 0);
            relation.assign(n, 0);
        }

        pair<int, int> find(int i) {
            if (parent[i] != i) {
                pair<int, int> rootInfo = find(parent[i]);
                parent[i] = rootInfo.first;
                // The relation of i to new root is (relation of i to old parent) XOR (relation of old parent to new root)
                relation[i] = relation[i] ^ rootInfo.second;
            }
            return {parent[i], relation[i]};
        }

        // Returns false if adding this edge creates an odd cycle (conflict)
        bool unionSets(int i, int j) {
            pair<int, int> rootI = find(i);
            pair<int, int> rootJ = find(j);
            
            int u = rootI.first;
            int v = rootJ.first;
            int relU = rootI.second;
            int relV = rootJ.second;

            if (u != v) {
                // Merge u into v
                parent[u] = v;
                // We want color(i) != color(j)
                // color(i) = relU ^ color(u)
                // color(j) = relV ^ color(v)
                // So: relU ^ color(u) != relV ^ color(v)
                // => relU ^ color(u) ^ relV ^ color(v) = 1
                // => color(u) ^ color(v) = 1 ^ relU ^ relV
                // The relation between u and v is what we store in relation[u]
                relation[u] = 1 ^ relU ^ relV;
                return true;
            } else {
                // Already in same component
                // Check for conflict: color(i) must differ from color(j)
                // i.e., relU must differ from relV relative to the common root
                if (relU == relV) {
                    return false; // Conflict found (odd cycle)
                }
                return true;
            }
        }
    };

public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;

        vector<Edge> edges;
        edges.reserve(n * (n - 1) / 2);

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long dist = (long long)abs(points[i][0] - points[j][0]) + 
                                 (long long)abs(points[i][1] - points[j][1]);
                edges.push_back({dist, i, j});
            }
        }

        sort(edges.begin(), edges.end());

        DSU dsu(n);
        for (const auto& edge : edges) {
            if (!dsu.unionSets(edge.u, edge.v)) {
                return edge.w;
            }
        }

        return 0;
    }
};
# @lc code=end