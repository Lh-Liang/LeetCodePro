#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // The threshold constraint (at most threshold outgoing edges) is always satisfied
        // if node 0 is reachable from all other nodes. This is because reachability
        // implies we can extract an in-tree rooted at node 0 where every node except 0
        // has an out-degree of 1. Since threshold >= 1, this satisfies the condition.
        
        int max_w = 0;
        vector<vector<pair<int, int>>> rev_adj(n);
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            // Reverse the edges: reachability to node 0 becomes reachability from node 0.
            rev_adj[v].push_back({u, w});
            if (w > max_w) max_w = w;
        }
        
        vector<int> visited(n, 0);
        int timer = 0;
        vector<int> q(n);
        
        auto can_reach_all = [&](int limit) {
            timer++;
            int head = 0, tail = 0;
            
            // BFS in the reversed graph starting from node 0.
            q[tail++] = 0;
            visited[0] = timer;
            int count = 1;
            
            while (head < tail) {
                int u = q[head++];
                for (const auto& edge : rev_adj[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (w <= limit && visited[v] != timer) {
                        visited[v] = timer;
                        count++;
                        if (count == n) return true;
                        q[tail++] = v;
                    }
                }
            }
            return count == n;
        };
        
        int low = 1, high = max_w;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (can_reach_all(mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
};
# @lc code=end