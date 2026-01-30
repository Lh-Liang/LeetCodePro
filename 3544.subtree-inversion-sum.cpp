#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        // dp[u][d] stores a pair: {max_sum with parity 0, max_sum with parity 1}
        // d: distance to nearest inverted ancestor (1 to k)
        vector<vector<pair<long long, long long>>> dp(n, vector<pair<long long, long long>>(k + 1));

        // Iterative post-order traversal to avoid stack overflow
        vector<int> order;
        vector<int> parent(n, -1);
        vector<int> stack = {0};
        parent[0] = 0; 
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            order.push_back(u);
            for (int v : adj[u]) {
                if (parent[v] == -1) {
                    parent[v] = u;
                    stack.push_back(v);
                }
            }
        }

        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            for (int d = 1; d <= k; ++d) {
                // Option 1: Don't invert current node u
                long long res0 = (long long)nums[u];  // inherited parity 0
                long long res1 = (long long)-nums[u]; // inherited parity 1
                
                for (int v : adj[u]) {
                    if (v == parent[u]) continue;
                    res0 += dp[v][min(k, d + 1)].first;
                    res1 += dp[v][min(k, d + 1)].second;
                }

                // Option 2: Invert node u (only if distance constraint d == k is met)
                if (d == k) {
                    long long inv0 = (long long)-nums[u]; // flip parity 0 -> 1
                    long long inv1 = (long long)nums[u];  // flip parity 1 -> 0
                    for (int v : adj[u]) {
                        if (v == parent[u]) continue;
                        inv0 += dp[v][1].second; // child sees inverted ancestor at dist 1, parity 1
                        inv1 += dp[v][1].first;  // child sees inverted ancestor at dist 1, parity 0
                    }
                    res0 = max(res0, inv0);
                    res1 = max(res1, inv1);
                }
                dp[u][d] = {res0, res1};
            }
        }

        // Result is max sum starting at root with no inverted ancestors (d=k, parity=0)
        return dp[0][k].first;
    }
};