#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#
# @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Build adjacency list
        vector<vector<int>> graph(n);
        for (auto& inv : invocations) {
            graph[inv[0]].push_back(inv[1]);
        }
        
        // Find all suspicious methods using BFS from k
        vector<bool> suspicious(n, false);
        queue<int> q;
        q.push(k);
        suspicious[k] = true;
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            for (int next : graph[curr]) {
                if (!suspicious[next]) {
                    suspicious[next] = true;
                    q.push(next);
                }
            }
        }
        
        // Check if we can remove suspicious methods
        bool canRemove = true;
        for (auto& inv : invocations) {
            int a = inv[0], b = inv[1];
            if (!suspicious[a] && suspicious[b]) {
                canRemove = false;
                break;
            }
        }
        
        // Return result
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
# @lc code=end