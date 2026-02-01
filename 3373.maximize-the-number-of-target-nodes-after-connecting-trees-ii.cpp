#
# @lc app=leetcode id=3373 lang=cpp
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;

        auto get_partition_info = [](int size, const vector<vector<int>>& adj) {
            vector<int> color(size, -1);
            vector<int> counts(2, 0);
            queue<int> q;
            
            color[0] = 0;
            counts[0]++;
            q.push(0);
            
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

        vector<vector<int>> adj1(n);
        for (const auto& e : edges1) {
            adj1[e[0]].push_back(e[1]);
            adj1[e[1]].push_back(e[0]);
        }

        vector<vector<int>> adj2(m);
        for (const auto& e : edges2) {
            adj2[e[0]].push_back(e[1]);
            adj2[e[1]].push_back(e[0]);
        }

        auto [color1, counts1] = get_partition_info(n, adj1);
        auto [color2, counts2] = get_partition_info(m, adj2);

        int max_tree2_contribution = max(counts2[0], counts2[1]);

        vector<int> answer(n);
        for (int i = 0; i < n; ++i) {
            answer[i] = counts1[color1[i]] + max_tree2_contribution;
        }

        return answer;
    }
};
# @lc code=end