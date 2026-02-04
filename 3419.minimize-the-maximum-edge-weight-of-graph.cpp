#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        int left = 1, right = 1e6, ans = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // Step 1: Filter edges by candidate weight
            vector<vector<int>> g(n);
            vector<int> out_deg(n, 0);
            for (const auto& e : edges) {
                if (e[2] <= mid) {
                    g[e[0]].push_back(e[1]);
                    out_deg[e[0]]++;
                }
            }
            // Step 2: Check outgoing edge count constraint independently
            bool valid = true;
            for (int i = 0; i < n; ++i) {
                if (out_deg[i] > threshold) {
                    valid = false;
                    break;
                }
            }
            if (!valid) {
                left = mid + 1;
                continue;
            }
            // Step 3: Check reachability independently in reversed graph
            vector<vector<int>> rev_g(n);
            for (int u = 0; u < n; ++u) {
                for (int v : g[u]) {
                    rev_g[v].push_back(u);
                }
            }
            vector<bool> vis(n, false);
            std::queue<int> q;
            q.push(0);
            vis[0] = true;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : rev_g[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        q.push(v);
                    }
                }
            }
            // Step 4: Verify all nodes reach node 0
            bool all_reach = true;
            for (int i = 0; i < n; ++i) {
                if (!vis[i]) {
                    all_reach = false;
                    break;
                }
            }
            // Step 5: Update answer or adjust binary search
            if (all_reach) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
};
# @lc code=end