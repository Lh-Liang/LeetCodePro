#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#
# @lc code=start
class Solution {
public:
    bool canAchieve(int n, vector<vector<int>>& edges, int threshold, int maxWeight) {
        // Build reverse adjacency list
        vector<vector<int>> revAdj(n);
        for (auto& e : edges) {
            if (e[2] <= maxWeight) {
                revAdj[e[1]].push_back(e[0]);
            }
        }
        
        // BFS from 0 in reverse graph
        vector<bool> reachable(n, false);
        queue<int> q;
        q.push(0);
        reachable[0] = true;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : revAdj[u]) {
                if (!reachable[v]) {
                    reachable[v] = true;
                    q.push(v);
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (!reachable[i]) return false;
        }
        return true;
    }
    
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        if (edges.empty()) return -1;
        
        // Get all unique weights and sort them
        set<int> weightSet;
        for (auto& e : edges) {
            weightSet.insert(e[2]);
        }
        vector<int> weights(weightSet.begin(), weightSet.end());
        
        // Binary search on the answer
        int left = 0, right = weights.size() - 1;
        int result = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canAchieve(n, edges, threshold, weights[mid])) {
                result = weights[mid];
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return result;
    }
};
# @lc code=end