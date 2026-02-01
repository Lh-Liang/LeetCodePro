#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution {
    struct Result {
        long long dp0;
        long long dp1;
    };

    Result dfs(int u, int p, int k, const vector<vector<pair<int, int>>>& adj) {
        long long base_sum = 0;
        vector<long long> diffs;
        
        for (const auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v == p) continue;
            
            Result res = dfs(v, u, k, adj);
            base_sum += res.dp0;
            long long diff = (res.dp1 + (long long)w) - res.dp0;
            if (diff > 0) {
                diffs.push_back(diff);
            }
        }
        
        sort(diffs.begin(), diffs.end(), greater<long long>());
        
        long long sum_diffs = 0;
        int i = 0;
        int n_diffs = (int)diffs.size();
        
        // Calculate dp1: at most k-1 edges to children
        for (; i < n_diffs && i < k - 1; ++i) {
            sum_diffs += diffs[i];
        }
        long long res1 = base_sum + sum_diffs;
        
        // Calculate dp0: at most k edges to children
        if (i < n_diffs && i < k) {
            sum_diffs += diffs[i];
        }
        long long res0 = base_sum + sum_diffs;
        
        return {res0, res1};
    }

public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = (int)edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        
        return dfs(0, -1, k, adj).dp0;
    }
};