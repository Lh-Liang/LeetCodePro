#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits.h>
using namespace std;
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<pair<int, pair<int, int>>>> graph;
        for (const auto& edge : edges) {
            int ui = edge[0], vi = edge[1], starti = edge[2], endi = edge[3];
            graph[ui].emplace_back(vi, make_pair(starti, endi));
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        vector<int> minTime(n, INT_MAX);
        pq.emplace(0, 0);
        minTime[0] = 0;
        while (!pq.empty()) {
            auto [time, node] = pq.top(); pq.pop();
            if (node == n - 1) return time;
            if (time > minTime[node]) continue;
            for (auto& [nextNode, interval] : graph[node]) {
                auto [starti, endi] = interval;
                int arrivalTime = max(time + 1, starti + 1);
                if (arrivalTime <= endi && arrivalTime < minTime[nextNode]) {
                    minTime[nextNode] = arrivalTime;
                    pq.emplace(arrivalTime, nextNode);
                }
            }
        }
        return -1;
    }
};
# @lc code=end