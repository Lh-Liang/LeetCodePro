#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        auto can = [&](int k) -> bool {
            if (k == 0) return true;
            if (n == 2) return false;
            vector<vector<int>> adj(n);
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    long long dx = abs((long long)points[i][0] - points[j][0]);
                    long long dy = abs((long long)points[i][1] - points[j][1]);
                    long long dist = dx + dy;
                    if (dist < k) {
                        adj[i].push_back(j);
                        adj[j].push_back(i);
                    }
                }
            }
            vector<int> color(n, -1);
            for (int i = 0; i < n; ++i) {
                if (color[i] != -1) continue;
                queue<int> q;
                color[i] = 0;
                q.push(i);
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : adj[u]) {
                        if (color[v] == -1) {
                            color[v] = 1 - color[u];
                            q.push(v);
                        } else if (color[v] == color[u]) {
                            return false;
                        }
                    }
                }
            }
            return true;
        };
        int left = 0;
        int right = 400000001;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (can(mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
# @lc code=end