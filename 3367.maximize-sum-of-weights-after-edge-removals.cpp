#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    struct State {
        long long kept_parent;
        long long removed_parent;
    };

    struct Edge {
        int to;
        int weight;
    };

    vector<vector<Edge>> adj;

    State dfs(int u, int p, int k) {
        long long base_sum = 0;
        vector<long long> positive_gains;

        for (const auto& edge : adj[u]) {
            if (edge.to == p) continue;
            
            State child_res = dfs(edge.to, u, k);
            
            // Always take the child's 'removed_parent' state as the baseline
            base_sum += child_res.removed_parent;
            
            // Calculate the marginal gain of keeping the edge to this child
            long long gain = (long long)edge.weight + child_res.kept_parent - child_res.removed_parent;
            if (gain > 0) {
                positive_gains.push_back(gain);
            }
        }

        // Sort gains descending to pick the best ones greedily
        sort(positive_gains.rbegin(), positive_gains.rend());

        long long res_kept = base_sum;
        long long res_removed = base_sum;

        // Calculate dp[u][0]: can take up to k-1 children
        for (int i = 0; i < (int)positive_gains.size() && i < k - 1; ++i) {
            res_kept += positive_gains[i];
        }

        // Calculate dp[u][1]: can take up to k children
        // Since we already calculated res_kept (up to k-1), we can derive res_removed easily
        res_removed = res_kept;
        if (positive_gains.size() >= k && k > 0) {
            res_removed += positive_gains[k - 1];
        } else if (positive_gains.size() == k - 1 && k > 0) {
            // Already covered by the loop above, but logic remains consistent
        } else if (positive_gains.size() < k - 1) {
            // Already covered by the loop above
        }
        
        // Correctly calculate res_removed by simply taking up to k elements
        res_removed = base_sum;
        for (int i = 0; i < (int)positive_gains.size() && i < k; ++i) {
            res_removed += positive_gains[i];
        }

        return {res_kept, res_removed};
    }

public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        int n = edges.size() + 1;
        adj.assign(n, {});
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        State root_res = dfs(0, -1, k);
        // At the root, there is no parent edge to keep, so we take the 'removed' state
        return root_res.removed_parent;
    }
};