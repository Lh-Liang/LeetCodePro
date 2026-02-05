#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#
# @lc code=start
class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        vector<vector<pair<int,int>>> adj(n); // node, edgeId
        vector<int> degree(n, 0);
        vector<int> toU(edges.size()), toV(edges.size()), weight(edges.size());
        for (int i = 0; i < edges.size(); ++i) {
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            adj[u].push_back({v, i});
            adj[v].push_back({u, i});
            degree[u]++; degree[v]++;
            toU[i] = u; toV[i] = v; weight[i] = w;
        }
        vector<bool> removed(edges.size(), false);
        for (int node = 0; node < n; ++node) {
            if (degree[node] > k) {
                vector<pair<int,int>> incEdges; // (weight, edgeId)
                for (auto& [nei, eid] : adj[node]) {
                    if (!removed[eid])
                        incEdges.push_back({weight[eid], eid});
                }
                sort(incEdges.begin(), incEdges.end());
                int toRemove = degree[node] - k;
                for (int j = 0, cnt = 0; cnt < toRemove && j < incEdges.size(); ++j) {
                    int eid = incEdges[j].second;
                    if (!removed[eid]) {
                        removed[eid] = true;
                        degree[toU[eid]]--;
                        degree[toV[eid]]--;
                        cnt++;
                    }
                }
            }
        }
        long long res = 0;
        for (int i = 0; i < edges.size(); ++i) {
            if (!removed[i]) res += weight[i];
        }
        return res;
    }
};
# @lc code=end