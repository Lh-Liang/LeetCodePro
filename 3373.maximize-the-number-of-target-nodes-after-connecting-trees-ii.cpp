#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;

        auto get_tree_info = [](int size, const vector<vector<int>>& edges) {
            vector<vector<int>> adj(size);
            for (const auto& e : edges) {
                adj[e[0]].push_back(e[1]);
                adj[e[1]].push_back(e[0]);
            }
            
            vector<int> color(size, -1);
            vector<int> counts(2, 0);
            queue<int> q;

            if (size > 0) {
                q.push(0);
                color[0] = 0;
                counts[0]++;
            }

            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        counts[color[v]]++;
                        q.push(v);
                    }
                }
            }
            return make_pair(color, counts);
        };

        auto [color1, counts1] = get_tree_info(n, edges1);
        auto [color2, counts2] = get_tree_info(m, edges2);

        int max_tree2 = max(counts2[0], counts2[1]);

        vector<int> answer(n);
        for (int i = 0; i < n; ++i) {
            answer[i] = counts1[color1[i]] + max_tree2;
        }

        return answer;
    }
};