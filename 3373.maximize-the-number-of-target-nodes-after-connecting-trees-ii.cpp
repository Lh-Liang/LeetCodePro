#
# @lc app=leetcode id=3373 lang=cpp
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = edges1.size() + 1, m = edges2.size() + 1;
        vector<vector<int>> g1(n), g2(m);
        for (auto &e : edges1) {
            g1[e[0]].push_back(e[1]);
            g1[e[1]].push_back(e[0]);
        }
        for (auto &e : edges2) {
            g2[e[0]].push_back(e[1]);
            g2[e[1]].push_back(e[0]);
        }
        auto getParity = [](vector<vector<int>>& g, int sz) {
            vector<int> parity(sz, -1);
            queue<int> q;
            parity[0] = 0;
            q.push(0);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : g[u]) {
                    if (parity[v] == -1) {
                        parity[v] = 1 - parity[u];
                        q.push(v);
                    }
                }
            }
            return parity;
        };
        vector<int> parity1 = getParity(g1, n);
        vector<int> parity2 = getParity(g2, m);
        int even1 = 0, odd1 = 0, even2 = 0, odd2 = 0;
        for (int x : parity1) {
            if (x == 0) even1++;
            else odd1++;
        }
        for (int x : parity2) {
            if (x == 0) even2++;
            else odd2++;
        }
        // Sanity check: parity group sizes sum to total node count
        assert(even1 + odd1 == n);
        assert(even2 + odd2 == m);
        int max2 = max(even2, odd2);
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = (parity1[i] == 0 ? even1 : odd1) + max2;
        }
        // Output validation
        assert(ans.size() == n);
        for (int x : ans) assert(x <= n + m && x >= 1);
        return ans;
    }
};
# @lc code=end