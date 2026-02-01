#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // The condition "Node 0 must be reachable from all other nodes" means that in the 
        // original graph, there must be a path from every node i to node 0.
        // If such paths exist, we can always select a subset of edges that forms a 
        // spanning tree directed towards node 0. In this tree, each node (except 0) 
        // has an out-degree of exactly 1.
        // Since threshold >= 1, this out-degree 1 always satisfies the condition 
        // "at most threshold outgoing edges".
        // Thus, we only need to find the minimum W such that reachability to node 0 
        // is maintained for all nodes.
        
        // Use a reversed adjacency list to check reachability from node 0 to all other nodes.
        vector<vector<pair<int, int>>> rev_adj(n);
        int max_w = 0;
        for (const auto& edge : edges) {
            int u = edge[0]; // source
            int v = edge[1]; // target
            int w = edge[2];
            rev_adj[v].push_back({u, w});
            if (w > max_w) max_w = w;
        }

        // BFS function to check if all nodes are reachable from node 0 in the reversed graph
        // using only edges with weight <= W.
        auto check = [&](int W) {
            if (W <= 0 && n > 1) return false;
            vector<bool> visited(n, false);
            queue<int> q;
            q.push(0);
            visited[0] = true;
            int count = 1;
            
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                
                for (const auto& edge : rev_adj[u]) {
                    int v = edge.first; // original source node
                    int w = edge.second;
                    if (w <= W && !visited[v]) {
                        visited[v] = true;
                        count++;
                        q.push(v);
                        if (count == n) return true;
                    }
                }
            }
            return count == n;
        };

        int low = 1, high = max_w;
        int ans = -1;

        // Binary search for the minimum possible maximum weight.
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
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