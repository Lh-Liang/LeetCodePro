#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

//
// @lc app=leetcode id=3419 lang=cpp
//
// [3419] Minimize the Maximum Edge Weight of Graph
//

// @lc code=start
class Solution {
public:
    /**
     * Helper function to check if node 0 can reach all other nodes in the 
     * reversed graph using only edges with weight <= maxW.
     */
    bool canReachAll(int maxW, int n, const vector<vector<pair<int, int>>>& revAdj) {
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
        int count = 1;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (const auto& edge : revAdj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (w <= maxW && !visited[v]) {
                    visited[v] = true;
                    count++;
                    q.push(v);
                    if (count == n) return true; // Early exit if all nodes reached
                }
            }
        }
        return count == n;
    }

    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // The threshold is at least 1. If reachability to node 0 is possible,
        // it can be achieved by a spanning tree where each node has out-degree 1.
        // Thus, the threshold constraint is implicitly satisfied if reachability is met.

        // Build the reversed adjacency list
        vector<vector<pair<int, int>>> revAdj(n);
        vector<int> uniqueWeights;
        for (const auto& e : edges) {
            revAdj[e[1]].push_back({e[0], e[2]});
            uniqueWeights.push_back(e[2]);
        }

        // Sort and get unique weights to optimize binary search range
        sort(uniqueWeights.begin(), uniqueWeights.end());
        uniqueWeights.erase(unique(uniqueWeights.begin(), uniqueWeights.end()), uniqueWeights.end());

        int low = 0, high = (int)uniqueWeights.size() - 1;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canReachAll(uniqueWeights[mid], n, revAdj)) {
                ans = uniqueWeights[mid];
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
};
// @lc code=end