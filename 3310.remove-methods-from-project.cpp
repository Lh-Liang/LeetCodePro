#
# @lc app=leetcode id=3310 lang=cpp
#
# [3310] Remove Methods From Project
#
# @lc code=start
class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // Step 1: Create a graph representation of method invocations
        unordered_map<int, vector<int>> graph;
        for (const auto& invocation : invocations) {
            graph[invocation[0]].push_back(invocation[1]);
        }
        
        // Step 2: Use BFS/DFS to find all methods reachable from k (suspicious methods)
        unordered_set<int> suspicious;
        queue<int> q;
        unordered_set<int> visited;
        q.push(k);
        while (!q.empty()) {
            int current = q.front(); q.pop();
            if (visited.find(current) == visited.end()) {
                visited.insert(current);
                suspicious.insert(current);
                for (int neighbor : graph[current]) {
                    if (visited.find(neighbor) == visited.end()) {
                        q.push(neighbor);
                    }
                }
            }
        }
        
        // Step 3: Check for any non-suspicious methods that invoke a suspicious method directly or indirectly.
        unordered_set<int> safeMethods;
        for (int i = 0; i < n; ++i) {
            if (suspicious.find(i) == suspicious.end()) { // not suspicious itself 
                bool invokesSuspicious = false; 
                queue<int> checkQueue; 
                unordered_set<int> checkVisited; 
                checkQueue.push(i); 
                while (!checkQueue.empty()) { 
                    int method = checkQueue.front(); checkQueue.pop(); 
                    if (checkVisited.find(method) != checkVisited.end()) continue; 
                    checkVisited.insert(method); 
                    if (suspicious.find(method) != suspicious.end()) { 
                        invokesSuspicious = true; break; 
                    } else { 
                        for (int neighbor : graph[method]) { 
                            if (checkVisited.find(neighbor) == checkVisited.end()) { 
                                checkQueue.push(neighbor); 
                            }
                        } 
                    } 
                } 
                if (!invokesSuspicious) safeMethods.insert(i); 
            } 
        } 
         return safeMethods.size() == n - suspicious.size() ? vector<int>(safeMethods.begin(), safeMethods.end()) : vector<int>();
    }
};
# @lc code=end