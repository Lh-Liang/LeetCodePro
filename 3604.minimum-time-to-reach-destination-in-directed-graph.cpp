#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
#include <vector>
#include <queue>
#include <unordered_map>
#include <climits>
using namespace std;

class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        // Build adjacency list: node -> list of (neighbor, start, end)
        vector<vector<tuple<int, int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].emplace_back(e[1], e[2], e[3]);
        }
        // min-heap: (arrival_time, node)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        vector<int> minTime(n, INT_MAX);
        pq.emplace(0, 0);
        minTime[0] = 0;
        while (!pq.empty()) {
            auto [curTime, u] = pq.top(); pq.pop();
            if (u == n - 1) {
                // Verify all constraints are satisfied before returning
                return curTime;
            }
            if (curTime > minTime[u]) continue;
            for (const auto& [v, start, end] : adj[u]) {
                // Validate edge's time window
                int depart = max(curTime, start);
                if (depart > end) continue;
                int arrive = depart + 1;
                if (arrive < minTime[v]) {
                    minTime[v] = arrive;
                    pq.emplace(arrive, v);
                }
            }
        }
        // If unreachable, return -1
        return -1;
    }
};
# @lc code=end