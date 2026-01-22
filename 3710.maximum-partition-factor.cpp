//
// @lc app=leetcode id=3710 lang=cpp
//
// [3710] Maximum Partition Factor
//
// @lc code=start
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;
        
        vector<long long> distances;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long long d = abs((long long)points[i][0] - points[j][0]) + abs((long long)points[i][1] - points[j][1]);
                distances.push_back(d);
            }
        }
        
        sort(distances.begin(), distances.end());
        distances.erase(unique(distances.begin(), distances.end()), distances.end());
        
        int lo = 0, hi = (int)distances.size() - 1;
        long long ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (canPartition(points, distances[mid])) {
                ans = distances[mid];
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        
        return (int)ans;
    }
    
    bool canPartition(vector<vector<int>>& points, long long threshold) {
        int n = points.size();
        vector<vector<int>> adj(n);
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long long d = abs((long long)points[i][0] - points[j][0]) + abs((long long)points[i][1] - points[j][1]);
                if (d < threshold) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }
        
        vector<int> color(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                queue<int> q;
                q.push(i);
                color[i] = 0;
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
        }
        
        return true;
    }
};
// @lc code=end