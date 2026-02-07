#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#
# @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Initialize adjacency lists for direct and reverse graphs
        vector<vector<int>> adjList(n), reverseAdjList(n);
        for (auto& invocation : invocations) {
            adjList[invocation[0]].push_back(invocation[1]);
            reverseAdjList[invocation[1]].push_back(invocation[0]);
        }
        
        // Perform BFS/DFS from method k to find all reachable/suspicious nodes
        vector<bool> isSuspicious(n, false);
        queue<int> q;
        q.push(k);
        isSuspicious[k] = true;
        while (!q.empty()) {
            int current = q.front(); q.pop();
            for (int neighbor : adjList[current]) {
                if (!isSuspicious[neighbor]) {
                    isSuspicious[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        // Check if any non-suspicious method invokes a suspicious one
        for (int i = 0; i < n; ++i) {
            if (!isSuspicious[i]) {
                for (int neighbor : reverseAdjList[i]) {
                    if (isSuspicious[neighbor]) {
                        // If any such invocation exists, we cannot safely remove the suspicious group.
                        return vector<int>(begin({0}), end({0}) + n); // return all methods
                    }
                }
            }
        }

        // Collect non-suspicious methods
        vector<int> remainingMethods;
        for (int i = 0; i < n; ++i) {
            if (!isSuspicious[i]) {
                remainingMethods.push_back(i);
            }
        }

        return remainingMethods;
    }
};
# @lc code=end