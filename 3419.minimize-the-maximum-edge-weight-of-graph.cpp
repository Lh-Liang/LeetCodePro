#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        auto can = [&](int maxw) -> bool {
            vector<vector<int>> rev(n);
            for (const auto& e : edges) {
                if (e[2] <= maxw) {
                    rev[e[1]].push_back(e[0]);
                }
            }
            vector<bool> visited(n, false);
            queue<int> q;
            q.push(0);
            visited[0] = true;
            int cnt = 1;
            while (!q.empty()) {
                int cur = q.front(); q.pop();
                for (int nxt : rev[cur]) {
                    if (!visited[nxt]) {
                        visited[nxt] = true;
                        ++cnt;
                        q.push(nxt);
                    }
                }
            }
            return cnt == n;
        };
        int l = 0, r = 1000000;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (can(m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return can(l) ? l : -1;
    }
};
# @lc code=end