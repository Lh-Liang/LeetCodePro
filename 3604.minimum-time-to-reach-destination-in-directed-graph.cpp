#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <climits>
using namespace std;
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        vector<unordered_map<int, vector<pair<int,int>>>> graph(n);
        for (auto &edge : edges) {
            int u = edge[0], v = edge[1], start = edge[2], end = edge[3];
            graph[u][v].push_back({start, end});
        }
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        pq.push({0, 0}); // start at node 0 at time 0
        vector<int> minTime(n, INT_MAX); // shortest time to reach each node
        minTime[0] = 0; // time to reach node 0 is 0 by definition
        while (!pq.empty()) {
            auto [currTime, u] = pq.top(); pq.pop();
            if (u == n-1) return currTime; // reached destination node n-1
            if (currTime > minTime[u]) continue; // skip if better path already found 
            for (auto &[v, periods] : graph[u]) { // explore neighbors v from u 
                for (auto &[start, end] : periods) { // check all available periods 
                    if (currTime >= start && currTime <= end) { // can travel this edge now? 
                        int nextTime = currTime + 1; // travel takes one unit of time 
                        if (nextTime < minTime[v]) { // found a quicker path? 
                            minTime[v] = nextTime; // update shortest path to v 
                            pq.push({nextTime, v}); // push updated path onto queue 
                        }}}}}return -1;}}; // @lc code=end