#
# @lc app=leetcode id=3367 lang=cpp
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    struct Edge {
        int to;
        int weight;
    };
    
    vector<vector<Edge>> adj;
    int K;

    struct Result {
        long long take_k_minus_1;
        long long take_k;
    };

    Result dfs(int u, int p) {
        long long base_sum = 0;
        vector<long long> diffs;

        for (auto& edge : adj[u]) {
            if (edge.to == p) continue;
            Result res = dfs(edge.to, u);
            
            // By default, assume we don't take the edge (u, edge.to).
            // The child is then free to use up to K edges within its own subtree.
            base_sum += res.take_k;
            
            // The benefit of taking the edge (u, edge.to):
            // If we take it, the child must limit itself to K-1 edges to its own children.
            // Benefit = (weight of (u, v) + child's max sum with K-1 edges) - child's max sum with K edges.
            long long d = (res.take_k_minus_1 + edge.weight) - res.take_k;
            if (d > 0) {
                diffs.push_back(d);
            }
        }

        sort(diffs.rbegin(), diffs.rend());

        long long sum_diffs = 0;
        int n_diffs = (int)diffs.size();
        
        // Case 1: Node u can take at most K-1 edges to its children (one slot reserved for parent edge)
        for (int i = 0; i < n_diffs && i < K - 1; ++i) {
            sum_diffs += diffs[i];
        }
        long long res_k_minus_1 = base_sum + sum_diffs;

        // Case 2: Node u can take at most K edges to its children (no parent edge)
        if (K - 1 < n_diffs && K - 1 >= 0) {
            sum_diffs += diffs[K - 1];
        }
        long long res_k = base_sum + sum_diffs;

        return {res_k_minus_1, res_k};
    }

public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        adj.assign(n, vector<Edge>());
        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        K = k;
        // Root the tree at node 0. Node 0 has no parent, so it can use up to K edges.
        return dfs(0, -1).take_k;
    }
};
# @lc code=end