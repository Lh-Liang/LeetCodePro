class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        return dfs(0, -1, k, adj).first;
    }

private:
    pair<long long, long long> dfs(int u, int p, int k, const vector<vector<pair<int, int>>>& adj) {
        long long base_sum = 0;
        vector<long long> deltas;

        for (const auto& edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (v == p) continue;

            pair<long long, long long> child_res = dfs(v, u, k, adj);
            
            // child_res.first is dp[v][0]: max weight if edge (u,v) is NOT kept
            // child_res.second is dp[v][1]: max weight if edge (u,v) IS kept (excluding w)
            
            base_sum += child_res.first;
            
            // Calculate the gain if we switch from removing (u, v) to keeping (u, v)
            long long gain = child_res.second + w - child_res.first;
            
            if (gain > 0) {
                deltas.push_back(gain);
            }
        }

        // Sort gains in descending order to pick the best ones greedily
        sort(deltas.rbegin(), deltas.rend());

        long long dp0 = base_sum;
        long long dp1 = base_sum;
        
        int m = deltas.size();
        
        // For dp0, we can take at most k children
        for (int i = 0; i < m && i < k; ++i) {
            dp0 += deltas[i];
        }
        
        // For dp1, we can take at most k-1 children
        for (int i = 0; i < m && i < k - 1; ++i) {
            dp1 += deltas[i];
        }
        
        return {dp0, dp1};
    }
};