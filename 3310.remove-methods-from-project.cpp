//
// @lc app=leetcode id=3310 lang=cpp
//
// [3310] Remove Methods From Project
//

// @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Build adjacency list
        vector<vector<int>> adj(n);
        for (auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }
        
        // Find all suspicious methods using BFS from k
        vector<bool> suspicious(n, false);
        queue<int> q;
        q.push(k);
        suspicious[k] = true;
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            for (int next : adj[curr]) {
                if (!suspicious[next]) {
                    suspicious[next] = true;
                    q.push(next);
                }
            }
        }
        
        // Check if any non-suspicious method invokes a suspicious method
        bool canRemove = true;
        for (auto& inv : invocations) {
            if (!suspicious[inv[0]] && suspicious[inv[1]]) {
                canRemove = false;
                break;
            }
        }
        
        // Build result
        vector<int> result;
        if (canRemove) {
            for (int i = 0; i < n; i++) {
                if (!suspicious[i]) {
                    result.push_back(i);
                }
            }
        } else {
            for (int i = 0; i < n; i++) {
                result.push_back(i);
            }
        }
        
        return result;
    }
};
// @lc code=end