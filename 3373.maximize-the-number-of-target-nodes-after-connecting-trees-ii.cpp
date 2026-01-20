#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;

        auto get_parity = [&](int size, vector<vector<int>>& edges) {
            vector<vector<int>> adj(size);
            for (auto& e : edges) {
                adj[e[0]].push_back(e[1]);
                adj[e[1]].push_back(e[0]);
            }
            vector<int> dist(size, -1);
            queue<int> q;
            q.push(0);
            dist[0] = 0;
            int count0 = 0, count1 = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                if (dist[u] % 2 == 0) count0++;
                else count1++;
                for (int v : adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return make_pair(dist, make_pair(count0, count1));
        };

        auto res1 = get_parity(n, edges1);
        vector<int> dist1 = res1.first;
        int c1_0 = res1.second.first;
        int c1_1 = res1.second.second;

        auto res2 = get_parity(m, edges2);
        int c2_0 = res2.second.first;
        int c2_1 = res2.second.second;
        int max_tree2 = max(c2_0, c2_1);

        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            if (dist1[i] % 2 == 0) {
                ans[i] = c1_0 + max_tree2;
            } else {
                ans[i] = c1_1 + max_tree2;
            }
        }

        return ans;
    }
};