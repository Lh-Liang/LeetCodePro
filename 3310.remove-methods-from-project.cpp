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
        for (const auto& inv : invocations) {
            graph[inv[0]].push_back(inv[1]);
        }
        
        // Find all suspicious methods using BFS from k
        unordered_set<int> suspicious;
        queue<int> q;
        q.push(k);
        suspicious.insert(k);
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            
            for (int next : graph[curr]) {
                if (suspicious.find(next) == suspicious.end()) {
                    suspicious.insert(next);
                    q.push(next);
                }
            }
        }
        
        // Check if any non-suspicious method invokes a suspicious method
        for (int i = 0; i < n; i++) {
            if (suspicious.find(i) == suspicious.end()) {
                // i is not suspicious
                for (int next : graph[i]) {
                    if (suspicious.find(next) != suspicious.end()) {
                        // Non-suspicious method invokes suspicious method
                        // Can't remove, return all methods
                        vector<int> result;
                        for (int j = 0; j < n; j++) {
                            result.push_back(j);
                        }
                        return result;
                    }
                }
            }
        }
        
        // Can remove all suspicious methods
        vector<int> result;
        for (int i = 0; i < n; i++) {
            if (suspicious.find(i) == suspicious.end()) {
                result.push_back(i);
            }
        }
        return result;
    }
};
# @lc code=end