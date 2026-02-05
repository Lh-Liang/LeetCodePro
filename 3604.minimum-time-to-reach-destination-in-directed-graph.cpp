#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
#include <vector>
#include <queue>
#include <limits>
using namespace std;
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        // Build adjacency list: node -> list of (neighbor, start, end)
        vector<vector<array<int,3>>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2], e[3]});
        }
        // min_time[node]: earliest time we've reached node
        vector<long long> min_time(n, numeric_limits<long long>::max());
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.emplace(0, 0); // (current_time, node)
        min_time[0] = 0;
        while (!pq.empty()) {
            auto [time, u] = pq.top(); pq.pop();
            if (u == n-1) return static_cast<int>(time);
            if (time > min_time[u]) continue;
            for (auto& [v, start, end] : adj[u]) {
                long long next_time = time < start ? start : time;
                if (next_time > end) continue;
                next_time += 1; // takes 1 unit time to travel
                if (next_time < min_time[v]) {
                    min_time[v] = next_time;
                    pq.emplace(next_time, v);
                }
            }
        }
        return -1;
    }
};
# @lc code=end