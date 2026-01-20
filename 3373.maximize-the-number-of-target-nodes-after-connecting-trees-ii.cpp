#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;

        auto get_parities = [&](int count, vector<vector<int>>& edges) {
            vector<vector<int>> adj(count);
            for (auto& edge : edges) {
                adj[edge[0]].push_back(edge[1]);
                adj[edge[1]].push_back(edge[0]);
            }
            vector<int> parity(count, -1);
            queue<int> q;
            q.push(0);
            parity[0] = 0;
            int even_count = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                if (parity[u] == 0) even_count++;
                for (int v : adj[u]) {
                    if (parity[v] == -1) {
                        parity[v] = 1 - parity[u];
                        q.push(v);
                    }
                }
            }
            return make_pair(parity, even_count);
        };

        auto [parity1, even1] = get_parities(n, edges1);
        auto [parity2, even2] = get_parities(m, edges2);

        int odd1 = n - even1;
        int odd2 = m - even2;
        int max_tree2_contribution = max(even2, odd2);

        vector<int> result(n);
        for (int i = 0; i < n; ++i) {
            int tree1_contribution = (parity1[i] == 0) ? even1 : odd1;
            result[i] = tree1_contribution + max_tree2_contribution;
        }

        return result;
    }
};