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

        auto getColors = [](int size, vector<vector<int>>& edges) {
            vector<vector<int>> adj(size);
            for (const auto& edge : edges) {
                adj[edge[0]].push_back(edge[1]);
                adj[edge[1]].push_back(edge[0]);
            }

            vector<int> colors(size, -1);
            int count0 = 0, count1 = 0;
            queue<int> q;
            
            colors[0] = 0;
            count0++;
            q.push(0);

            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    if (colors[v] == -1) {
                        colors[v] = 1 - colors[u];
                        if (colors[v] == 0) count0++;
                        else count1++;
                        q.push(v);
                    }
                }
            }
            return make_pair(colors, make_pair(count0, count1));
        };

        auto res1 = getColors(n, edges1);
        vector<int> colors1 = res1.first;
        int E1 = res1.second.first;
        int O1 = res1.second.second;

        auto res2 = getColors(m, edges2);
        int E2 = res2.second.first;
        int O2 = res2.second.second;
        int maxOddTree2 = max(E2, O2);

        vector<int> answer(n);
        for (int i = 0; i < n; ++i) {
            if (colors1[i] == 0) {
                answer[i] = E1 + maxOddTree2;
            } else {
                answer[i] = O1 + maxOddTree2;
            }
        }

        return answer;
    }
};
# @lc code=end